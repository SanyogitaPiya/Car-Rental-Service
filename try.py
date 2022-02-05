from tkinter import *
import tkinter.messagebox

import sqlite3

#Base root window
root = Tk()

root.title("Car Rental Service Database")
root.geometry("400x400")


#Task2:
#Requirement 1
def openInsertCustWindow():
    insertCustWindow = Toplevel(root)
    insertCustWindow.title("Add Information about new customer")
    insertCustWindow.geometry("400x400")
    
    def submit():
        submit_conn = sqlite3.connect("Project2")
        submit_cur = submit_conn.cursor()
    
        submit_cur.execute("SELECT * FROM CUSTOMER")
        rows = submit_cur.fetchall()
        size = len(rows)
        row = rows[size-1]
        custId = row[0]
        custId += 1
    
        submit_cur.execute("INSERT INTO CUSTOMER VALUES(:custId, :name, :phone)",
                                        {
                                            'custId': custId,
                                            'name': name.get(),
                                            'phone': phone.get()
                                        })
                                    
        submit_conn.commit()
        submit_conn.close()
    
    
    name = Entry(insertCustWindow, width = 30)
    name.grid(row = 0, column = 1, padx = 20) 

    phone = Entry(insertCustWindow, width = 30)
    phone.grid(row = 1, column = 1, padx = 20)



    name_label = Label(insertCustWindow, text = "Name: ")
    name_label.grid(row = 0, column = 0)

    phone_label = Label(insertCustWindow, text = "Phone: ")
    phone_label.grid(row = 1, column = 0)

    submit_button = Button(insertCustWindow, text = "Insert Info into CUSTOMER", command = submit)
    submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    
    
    
    
#Requirement 2
def openInsertVehicleWindow():
    insertVehicleWindow = Toplevel(root)
    insertVehicleWindow.title("Add Information about new vehicle")
    insertVehicleWindow.geometry("400x400")
    
    def submit():
        submit_conn = sqlite3.connect("Project2")
        submit_cur = submit_conn.cursor()
    
        submit_cur.execute("INSERT INTO VEHICLE VALUES(:vehicleId, :description, :year, :type, :category)",
                                        {
                                            'vehicleId': vehicleId.get(),
                                            'description': description.get(),
                                            'year': year.get(),
                                            'type': type.get(),
                                            'category': category.get()
                                        })
                                    
        submit_conn.commit()
        submit_conn.close()
        
    #Entry Fields
    vehicleId = Entry(insertVehicleWindow, width = 30)
    vehicleId.grid(row = 0, column = 1) 

    description = Entry(insertVehicleWindow, width = 30)
    description.grid(row = 1, column = 1)
    
    year = Entry(insertVehicleWindow, width = 5)
    year.grid(row = 2, column = 1, padx = 0)
    
    type = Entry(insertVehicleWindow, width = 5)
    type.grid(row = 3, column = 1)
    
    category = Entry(insertVehicleWindow, width = 5)
    category.grid(row = 4, column = 1)
    
    #Entry Labels
    vehicleId_label = Label(insertVehicleWindow, text = "VehicleID: ")
    vehicleId_label.grid(row = 0, column = 0)

    description_label = Label(insertVehicleWindow, text = "Description: ")
    description_label.grid(row = 1, column = 0)
    
    year_label = Label(insertVehicleWindow, text = "Year: ")
    year_label.grid(row = 2, column = 0)
    
    type_label = Label(insertVehicleWindow, text = "Type: ")
    type_label.grid(row = 3, column = 0)
    
    category_label = Label(insertVehicleWindow, text = "Category: ")
    category_label.grid(row = 4, column = 0)
    
    #Submit button
    submit_button = Button(insertVehicleWindow, text = "Insert Info into VEHICLE", command = submit)
    submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    
    
    
 #Requirement 3:
def openRentVehicleWindow():
    openVehicleWindow = Toplevel(root)
    openVehicleWindow.title("Rent a new vehicle")
    openVehicleWindow.geometry("400x400")
    
    def submit():
        submit_conn = sqlite3.connect("Project2")
        submit_cur = submit_conn.cursor()
        
        submit_cur.execute("SELECT V.Description, V.VehicleID FROM RENTAL AS R JOIN VEHICLE AS V ON R.VehicleID = V.VehicleID WHERE V.Type = ? AND V.Category = ? AND (R.StartDate < ? OR R.StartDate > ?) AND (R.ReturnDate < ? OR R.ReturnDate > ?)", (type.get(), category.get(), startDate.get(), returnDate.get(), startDate.get(), returnDate.get()))
        
        records = submit_cur.fetchall()
        
        
        if len(records) == 0:
            tkMessageBox.showerror('Error', 'No Vehicle of that type and category available for that time period.')
        else:
            for record in records:
                if record[0] == vehicleName.get():
                    submit_cur.execute("INSERT INTO RENTAL VALUES(:custId, :vehicleId, :startDate, :orderDate, :rentalType, :qty, :returnDate, :totalAmount, :paymentDate, :returned)",
                                        {
                                            'custId': custId.get(),
                                            'vehicleId': record[1],
                                            'startDate': startDate.get(),
                                            'orderDate': orderDate.get(),
                                            'rentalType': rentalType.get(),
                                            'qty': qty.get(),
                                            'returnDate': returnDate.get(),
                                            'totalAmount': None,
                                            'paymentDate': paymentDate.get(),
                                            'returned': 0
                                        })
                                        
                    break

            submit_conn.commit()
            submit_conn.close() 
        
        
    #Entry Fields
    custId = Entry(openVehicleWindow, width = 20)
    custId.grid(row = 0, column = 1)
    
    vehicleName = Entry(openVehicleWindow, width = 20)
    vehicleName.grid(row = 1, column = 1)
    
    startDate = Entry(openVehicleWindow, width = 20)
    startDate.grid(row = 2, column = 1)
    
    returnDate = Entry(openVehicleWindow, width = 20)
    returnDate.grid(row = 3, column = 1)
    
    orderDate = Entry(openVehicleWindow, width = 20)
    orderDate.grid(row = 4, column = 1)
    
    type = Entry(openVehicleWindow, width = 5)
    type.grid(row = 5, column = 1)
    
    category = Entry(openVehicleWindow, width = 5)
    category.grid(row = 6, column = 1)
    
    rentalType = Entry(openVehicleWindow, width = 5)
    rentalType.grid(row = 7, column = 1)
    
    qty = Entry(openVehicleWindow, width = 5)
    qty.grid(row = 8, column = 1)
    
    paymentDate = Entry(openVehicleWindow, width = 20)
    paymentDate.grid(row = 9, column = 1)
    
    #Entry Labels    
    custId_label = Label(openVehicleWindow, text = "Customer ID: ")
    custId_label.grid(row = 0, column = 0)
    
    vehicleName_label = Label(openVehicleWindow, text = "Vehicle Name: ")
    vehicleName_label.grid(row = 1, column = 0)
    
    startDate_label = Label(openVehicleWindow, text = "Start Date: ")
    startDate_label.grid(row = 2, column = 0)
    
    returnDate_label = Label(openVehicleWindow, text = "Return Date: ")
    returnDate_label.grid(row = 3, column = 0)
    
    orderDate_label = Label(openVehicleWindow, text = "Today's Date: ")
    orderDate_label.grid(row = 4, column = 0)
    
    type_label = Label(openVehicleWindow, text = "Car Type: ")
    type_label.grid(row = 5, column = 0)
    
    category_label = Label(openVehicleWindow, text = "Car Category: ")
    category_label.grid(row = 6, column = 0)
    
    rentalType_label = Label(openVehicleWindow, text = "Car Rental Type: ")
    rentalType_label.grid(row = 7, column = 0)
    
    qty_label_label = Label(openVehicleWindow, text = "Number: ")
    qty_label_label.grid(row = 8, column = 0)
    
    paymentDate_label = Label(openVehicleWindow, text = "Payment Date: ")
    paymentDate_label.grid(row = 9, column = 0)

    
    
    #Submit Button
    submit_button = Button(openVehicleWindow, text = "Rent a new VEHICLE", command = submit)
    submit_button.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    
    
    #Index Labels
    label1 = "\n" + "Car Type: 1 for Compact, 2 for Medium, 3 for Large, 4 for SUV , 5 for Truck, 6 for VAN" + "\n"
    label2 = "Car Category: 0 for Basic, 1 for Luxury" + "\n"
    label3 = "Car Rental Type: 1 for daily and 7 for weekly" + "\n"
    label4 = "Payment Date will be today's date if payment is going to be done today" + "\n"
    label5 = "Payment Date will be return date if payment is going to be done at the time of return" + "\n"
    label = label1 + label2 + label3 + label4 + label5
    
    output_label = Label(openVehicleWindow, text = label, justify = "center")
    output_label.grid(row = 14, column = 0)
    



#Requirement 4:
def openReturnRentedVehicleWindow():
    returnVehicleWindow = Toplevel(root)
    returnVehicleWindow.title("Rent a new vehicle")
    returnVehicleWindow.geometry("400x400")
    
    def submit():
        submit_conn = sqlite3.connect("Project2")
        submit_cur = submit_conn.cursor()
        
        submit_cur.execute("SELECT C.CustId, V.VehicleID, R.TotalAmount FROM RENTAL AS R JOIN VEHICLE AS V ON R.VehicleID = V.VehicleID JOIN CUSTOMER AS C ON C.CustId = R.CustId WHERE C.Name = ? AND V.Description = ? AND R.ReturnDate = ?", (custName.get(), vehicleName.get(), returnDate.get()))
        
        records = submit_cur.fetchall()
        record = records[0]
        
        submit_cur.execute("UPDATE RENTAL SET Returned = 1 WHERE CustID = ? AND VehicleID = ?", (record[0], str(record[1])))
        submit_conn.commit()
        submit_conn.close()
        
        output = str("\n" + "The total customer due for the rental is $" + str(record[2]) + "\n")        
        output_label = Label(returnVehicleWindow, text = output)
        output_label.grid(row = 6, column = 0, columnspan = 2)
        
        

    #Entry Fields
    custName = Entry(returnVehicleWindow, width = 20)
    custName.grid(row = 0, column = 1)
    
    returnDate = Entry(returnVehicleWindow)
    returnDate.grid(row = 1, column = 1)
    
    vehicleName = Entry(returnVehicleWindow)
    vehicleName.grid(row = 2, column = 1)
    
    
    #Entry Labels
    custName_label = Label(returnVehicleWindow, text = "Customer Name: ")
    custName_label.grid(row = 0, column = 0)
    
    returnDate_label = Label(returnVehicleWindow, text = "Return Date: ")
    returnDate_label.grid(row = 1, column = 0)
    
    vehicleName_label = Label(returnVehicleWindow, text = "Vehicle Name: ")
    vehicleName_label.grid(row = 2, column = 0)
    
    #Submit Button
    submit_button = Button(returnVehicleWindow, text = "Return Rented VEHICLE", command = submit)
    submit_button.grid(row = 4, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    

    
#Requirement 5A    
def openSearchBox():
    Open_search_query_conn=sqlite3.connect('Project2')
    Open_search_query_cur=Open_search_query_conn.cursor()
    searchBox = Toplevel(root)
    searchBox.title("Search IT")
    searchBox.geometry("700x700")
    
    def search_query():
        search_query_conn=sqlite3.connect('Project2')
        search_query_cur=search_query_conn.cursor()
        
        view_Name = search_Name.get()
        view_ID = search_ID.get()
        
        if (len(view_Name)==0 and len(view_ID)==0):
            search_query_cur.execute("SELECT VV.CustomerID, VV.CustomerName, CASE WHEN VV.RentalBalance IS NOT NULL THEN '$'||ROUND(VV.RentalBalance,2) WHEN VV.RentalBalance IS NULL THEN '$0.00' END AS Amount_Due FROM vRentalInfo VV ORDER BY VV.RentalBalance DESC")
                        
        else:
           search_query_cur.execute("SELECT VV.CustomerID, VV.CustomerName, CASE WHEN VV.RentalBalance IS NOT NULL THEN '$'||ROUND(VV.RentalBalance,2) END AS Amount_Due  FROM vRentalInfo VV WHERE VV.CustomerID = ? OR VV.CustomerName = ? OR VV.CustomerName LIKE '%"+view_Name+"%'",(view_ID, view_Name,))
        
        search_storage = search_query_cur.fetchall()
        apple = ''
        for pie in search_storage:
            apple =apple + str(pie) + "\n"
            
        #print('\n'+apple)
        label_for_rows=Label(searchBox,text='The number of rows are:'+ str(len(search_storage)))
        label_for_rows.grid(row=6,column=0)
        label_for_info = Label(searchBox, text=apple)
        label_for_info.grid(row=8, column=1,columnspan=2)
        
        search_query_conn.commit();
        search_query_conn.close();
    
    #create box to search
    search_ID=Entry(searchBox, width=30)
    search_ID.grid(row=0,column=1,padx=20)
    
    search_Name=Entry(searchBox, width=30)
    search_Name.grid(row=1,column=1,padx=20)
    
    #create label for them
    search_ID_label=Label(searchBox,text='Cust ID: ')
    search_ID_label.grid(row=0,column=0)
    
    search_FName_label=Label(searchBox,text='Name: ')
    search_FName_label.grid(row=1,column=0)
    
    
    #create button to search database
    btn = Button(searchBox, text="Search the Database",command=search_query)
    btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
    
    #Open_search_query_conn.commit();
    Open_search_query_conn.close();
    

#Requirement 5B
def openSearchBox2():
    Open_search_query_conn=sqlite3.connect('Project2')
    Open_search_query_cur=Open_search_query_conn.cursor()
    searchBox = Toplevel(root)
    searchBox.title("Search Vehicles")
    searchBox.geometry("700x700")
    
    def search_query():
        search_query_conn=sqlite3.connect('Project2')
        search_query_cur=search_query_conn.cursor()
        
        view_Description = search_Description.get()
        view_VIN = search_VIN.get()
        
        if (len(view_Description)==0 and len(view_VIN)==0):
            search_query_cur.execute("SELECT DISTINCT V.VehicleID AS VIN, V.Description, CASE WHEN R.TotalAmount IS NOT NULL THEN CASE WHEN R.RentalType=1 THEN '$'||round((R.TotalAmount/R.Qty),2) ELSE '$'||round((R.TotalAmount/(R.Qty*7)),2)END ELSE 'Non-Applicable' END AS Avg_Daily_Price FROM VEHICLE V LEFT OUTER JOIN RENTAL R ON V.VehicleID = R.VehicleID ORDER BY (CASE WHEN R.RentalType=1 THEN (R.TotalAmount/R.Qty) ELSE (R.TotalAmount/(R.Qty*7))END) ASC")
        else:
            search_query_cur.execute("SELECT DISTINCT V.VehicleID AS VIN, V.Description, CASE WHEN R.TotalAmount IS NOT NULL THEN CASE WHEN R.RentalType=1 THEN '$'||ROUND((R.TotalAmount/R.Qty),2) ELSE '$'||ROUND((R.TotalAmount/(R.Qty*7)),2)END ELSE 'Non-Applicable' END AS Avg_Daily_Price FROM VEHICLE V LEFT OUTER JOIN RENTAL R ON V.VehicleID = R.VehicleID WHERE V.VehicleID = ? OR V.Description = ? OR V.Description LIKE '%"+view_Description+"%'",(view_VIN,view_Description,))
        
        search_storage = search_query_cur.fetchall()
        apple = ''
        for pie in search_storage:
            apple =apple + str(pie) + "\n"
            
        #print('\n'+apple)
        label_for_rows=Label(searchBox,text='The number of rows are:'+ str(len(search_storage)))
        label_for_rows.grid(row=8,column=0)
        label_for_info = Label(searchBox, text=apple)
        label_for_info.grid(row=10, column=1, columnspan=2)
        
        #search_query_conn.commit();
        search_query_conn.close();
        
    
        
    #create box to search
    search_VIN=Entry(searchBox, width=30)
    search_VIN.grid(row=3,column=1,padx=20)
    
    search_Description=Entry(searchBox, width=30)
    search_Description.grid(row=4,column=1,padx=20)
    
    #create label for them
    search_VIN_label=Label(searchBox,text='VIN: ')
    search_VIN_label.grid(row=3,column=0)
    
    search_Description_label=Label(searchBox,text='Vehicle Description: ')
    search_Description_label.grid(row=4,column=0)
    
    #create button to search database
    btn = Button(searchBox, text="Search the Database",command=search_query)
    btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
    
    #Open_search_query_conn.commit();
    Open_search_query_conn.close();
    
    


#Main Window Buttons
btn1 = Button(root, text = "Click to add information about new customer", command = openInsertCustWindow)
btn1.grid(row = 0, column = 0)

btn2 = Button(root, text = "Click to add information about a new vehicle", command = openInsertVehicleWindow)
btn2.grid(row = 1, column = 0)

btn3 = Button(root, text = "Click to rent new vehicle", command = openRentVehicleWindow)
btn3.grid(row = 2, column = 0)

btn4 = Button(root, text = "Click to return rented vehicle", command = openReturnRentedVehicleWindow)
btn4.grid(row = 3, column = 0)

btn5 = Button(root, text="Click to search for name ID and balance",command=openSearchBox)
btn5.grid(row=4,column=0)

btn6 = Button(root, text="Click to search for vehicles",command=openSearchBox2)
btn6.grid(row=5,column=0)




#Main component that fires the whole application
root.mainloop()
