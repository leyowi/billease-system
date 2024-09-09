from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Materials:
    def __init__(self, root):
        self.root=root
        self.root.title("BillEase System")
        self.root.geometry("1540x800+0+0")

        self.date = StringVar()
        self.company = StringVar()
        self.attention = StringVar()
        self.email = StringVar()
        self.cc = StringVar()
        self.address = StringVar()
        self.telephone = StringVar()
        self.fax = StringVar()
        self.re = StringVar()

        self.item = StringVar()
        self.nameofbrand = StringVar()
        self.model = StringVar()
        self.serial = StringVar()
        self.disc = StringVar()
        self.qty = StringVar()
        self.unit = StringVar()

        lblltitle=Label(self.root, bd=20, relief=RIDGE, text="BillEase System", 
                        fg="green",bg="white", font=("Arial",50,"bold"))
        lblltitle.pack(side=TOP, fill=X)

        # ====================Left Frame====================== 
        Dataframe=Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x= 0, y= 120, width=615, height=665     )

        dataFrameInfo = LabelFrame(Dataframe, bd=10, relief= RIDGE, padx = 10, 
                                   font=("Arial",12,"bold"), text=" Information ", fg="green")
        dataFrameInfo.place(x= 5, y=5, width=258, height=340)

        dataFrameCL = LabelFrame(Dataframe, bd=10, relief= RIDGE, padx = 10,
                                    font=("Arial",12, "bold"), text=" Company List ", fg="green") 
        dataFrameCL.place(x= 270, y=5, width=300, height=340)

        inputFrame = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                    font=("Arial", 12, "bold"), text= " Input / Edit Data ", fg="green") 
        inputFrame.place(x=5, y=355, width=258, height=265)

        optionsFrame = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                    font=("Arial", 12, "bold"), text= " Sets / Options ", fg="green") 
        optionsFrame.place(x=270, y=355, width= 300, height=265)


        # ====================Information Data===================
        lblDate=Label(dataFrameInfo, text="Date", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblDate.grid(row=0, column=0, sticky=W)
        txtDate=Entry(dataFrameInfo, textvariable=self.date, font=("times new roman", 10), width=20)
        txtDate.grid(row=0, column=1)

        lblCompany=Label(dataFrameInfo, text="Company Name", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblCompany.grid(row=1, column=0, sticky=W)
        txtCompany=Entry(dataFrameInfo, textvariable=self.company, font=("times new roman", 10), width=20)
        txtCompany.grid(row=1, column=1)

        lblAtt=Label(dataFrameInfo, text="Attention", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblAtt.grid(row=2, column=0, sticky=W)
        txtAtt=Entry(dataFrameInfo, textvariable=self.attention, font=("times new roman", 10), width=20)
        txtAtt.grid(row=2, column=1)

        lblEmail=Label(dataFrameInfo, text="Email", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblEmail.grid(row=3, column=0, sticky=W)
        txtEmail=Entry(dataFrameInfo, textvariable=self.email, font=("times new roman", 10), width=20)
        txtEmail.grid(row=3, column=1)

        lblCc=Label(dataFrameInfo, text="Cc", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblCc.grid(row=4, column=0, sticky=W)
        txtCc=Entry(dataFrameInfo, textvariable=self.cc, font=("times new roman", 10), width=20)
        txtCc.grid(row=4, column=1)

        lblAdd=Label(dataFrameInfo, text="Address", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblAdd.grid(row=5, column=0, sticky=W)
        txtAdd=Entry(dataFrameInfo, textvariable=self.address, font=("times new roman", 10), width=20)
        txtAdd.grid(row=5, column=1)

        lblTel=Label(dataFrameInfo, text="Telephone", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblTel.grid(row=6, column=0, sticky=W)
        txtTel=Entry(dataFrameInfo, textvariable=self.telephone, font=("times new roman", 10), width=20)
        txtTel.grid(row=6, column=1)

        lblFax=Label(dataFrameInfo, text="Fax", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblFax.grid(row=7, column=0, sticky=W)
        txtFax=Entry(dataFrameInfo, textvariable=self.fax, font=("times new roman", 10), width=20)
        txtFax.grid(row=7, column=1)

        lblRe=Label(dataFrameInfo, text="Re", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblRe.grid(row=8, column=0, sticky=W)
        txtRe=Entry(dataFrameInfo, textvariable=self.re, font=("times new roman", 10), width=20)
        txtRe.grid(row=8, column=1)

        # BUTTONS 

        btnEnter1=Button(dataFrameInfo, text= "Enter", font=("arial", 8, "bold"), bg="light green", padx=3,pady=3)
        btnEnter1.grid(row=9, column=1)

        btnSave1=Button(dataFrameInfo, text= "Save", font=("arial", 8, "bold"), bg="light green", padx=3,pady=3)
        btnSave1.grid(row=9, column=0)

        # ==================== COMPANY LIST =====================
        scroll_c=ttk.Scrollbar(dataFrameCL, orient=VERTICAL)

        self.company_list=ttk.Treeview(dataFrameCL, column=("num", "nameofcompany"), yscrollcommand=scroll_c.set)
        
        scroll_c.pack(side = RIGHT, fill=Y)

        scroll_c.config(command=self.company_list.yview)

        self.company_list.heading("num", text= "") 
        self.company_list.heading("nameofcompany", text= "Company Name")
       

        self.company_list["show"] = "headings"
        self.company_list.pack(fill=BOTH, expand=1)

        self.company_list.column("num", width=0)
        self.company_list.column("nameofcompany", width=100)


        self.company_list.pack(fill=BOTH, expand=1)


        # ====================Input / Edit Data=====================

        lblItem=Label(inputFrame, text="Item", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblItem.grid(row=0, column=0, sticky=W)
        txtItem=Entry(inputFrame, textvariable=self.item, font=("times new roman", 10), width=20)
        txtItem.grid(row=0, column=1) 

        lblBrand=Label(inputFrame, text="Brand", font=("times new roman", 10, "bold"), padx = 2)
        lblBrand.grid(row=1, column=0, sticky=W)
        txtBrand=Entry(inputFrame, textvariable=self.nameofbrand, font=("times new roman", 10), width=20)
        txtBrand.grid(row=1, column=1)

        lblModel=Label(inputFrame, text="Model", font=("times new roman", 10, "bold"), padx = 2, pady = 4)
        lblModel.grid(row=2, column=0, sticky=W)
        txtModel=Entry(inputFrame, textvariable=self.model, font=("times new roman", 10), width=20)
        txtModel.grid(row=2, column=1)

        lblSerial=Label(inputFrame, text="Serial #", font=("times new roman", 10, "bold"), padx = 2, pady = 4)
        lblSerial.grid(row=3, column=0, sticky=W)
        txtSerial=Entry(inputFrame, textvariable=self.serial, font=("times new roman", 10), width=20)
        txtSerial.grid(row=3, column=1)

        lblDisc=Label(inputFrame, text="Discription", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblDisc.grid(row=4, column=0, sticky=W)
        txtDisc=Entry(inputFrame, textvariable=self.disc, font=("times new roman", 10), width=20)
        txtDisc.grid(row=4, column=1)

        lblQty=Label(inputFrame, text="Quantity", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblQty.grid(row=5, column=0,  sticky=W)
        txtQty=Entry(inputFrame, textvariable=self.qty, font=("times new roman", 10), width=20)
        txtQty.grid(row=5, column=1)

        lblUoM=Label(inputFrame, text="UOM", font=("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblUoM.grid(row=6, column=0,  sticky=W)
        # txtUoM=Entry(inputFrame, textvariable=self.unit, font=("times new roman", 10), width=20)
        # txtUoM.grid(row=6, column=1)    
        comUoM=ttk.Combobox(inputFrame, state="readonly",  textvariable=self.unit,
                            font=("times new roman", 10), width=17)
        comUoM['value']=("unit/s", "lot/s")
        comUoM.grid(row=6, column=1)

        # ==================== OPTIONS FRAME =====================
        
        scroll_o=ttk.Scrollbar(optionsFrame, orient=VERTICAL)

        self.set_list=ttk.Treeview(optionsFrame, column=("set", "nameofset"), yscrollcommand=scroll_o.set)
        
        scroll_o.pack(side = RIGHT, fill=Y)

        scroll_o.config(command=self.set_list.yview)

        self.set_list.heading("set", text= "") 
        self.set_list.heading("nameofset", text= "Options")
       

        self.set_list["show"] = "headings"

        self.set_list.column("set", width=0)
        self.set_list.column("nameofset", width=100)

        self.set_list.pack(fill=X, expand=0)

        # btnEditSet=Button(optionsFrame, text= "Set", font=("arial", 8, "bold"), bg="light green", padx= 12, width= 7)
        # btnEditSet.pack(side="bottom")


        # ====================Right Frame=====================
        Dataframe2 = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe2.place(x= 615, y= 120, width=912, height=665)
        tableFrame = LabelFrame(Dataframe2, bd=10, relief= RIDGE, padx = 10, 
                                   font=("Arial",12,"bold"), text=" Table ", fg="green")
        tableFrame.place(x= 5, y=5, width=860, height=615)


        # BUTTONS
        btnAdd = Button(inputFrame, text= "Add", font=("arial", 8, "bold"), bg="light green", padx=3,pady=3, command=self.iAdd)
        btnAdd.grid(row=7, column=1)

        btnUpd = Button(inputFrame, text= "Update", font=("arial", 8, "bold"), bg="light green", padx=3,pady=3, command=self.update_data)
        btnUpd.grid(row=7, column=0)

        btnDel = Button(inputFrame, text= "Del", font=("arial", 8, "bold"), bg="light green", padx=3,pady=3, command=self.idelete)
        btnDel.grid(row=7, column=2)




        # SCROLL BAR
        scroll_y=ttk.Scrollbar(tableFrame, orient=VERTICAL)

        self.materials_table=ttk.Treeview(tableFrame, column=("item", "nameofbrand", "model", "serial", "disc", "qty", "unit"), 
                                          yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side = RIGHT, fill=Y)

        scroll_y.config(command=self.materials_table.yview)

        self.materials_table.heading("item", text= "Item") 
        self.materials_table.heading("nameofbrand", text= "Brand")
        self.materials_table.heading("model", text= "Model")
        self.materials_table.heading("serial", text= "Serial Number")
        self.materials_table.heading("disc", text= "Discription")
        self.materials_table.heading("qty", text= "Quantity")
        self.materials_table.heading("unit", text= "UOM")

        self.materials_table["show"] = "headings"
        
        self.materials_table.column("item", width=15)
        self.materials_table.column("nameofbrand", width=50)
        self.materials_table.column("model", width=50)
        self.materials_table.column("serial", width=70)
        self.materials_table.column("disc", width=200)
        self.materials_table.column("qty", width=35)
        self.materials_table.column("unit", width=35)

        self.materials_table.pack(fill=BOTH, expand=1)

        self.materials_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fatch_data()


    # ====================FUNCTIONALITY=====================
    def iAdd(self):
        if self.item.get() == "" or self.nameofbrand.get() == "":
            messagebox.showerror("Error", "No blanks allowed")
        else:
            conn = mysql.connector.connect(host="localhost", 
                                           username="root", 
                                           password="palmeranthony", 
                                           database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into materials values (%s, %s, %s, %s, %s, %s, %s)"
                              ,(self.item.get(),
                                self.nameofbrand.get(),
                                self.model.get(),
                                self.serial.get(),
                                self.disc.get(),
                                self.qty.get(),
                                self.unit.get(),
                                ))
            conn.commit()
            self.fatch_data
            conn.close()
            messagebox.showinfo("Success", "Done")
    
    def update_data(self):
        if self.item.get() == "" or self.nameofbrand.get() == "":
            messagebox.showerror("Error", "No blanks allowed")
        else:
            conn = mysql.connector.connect(host="localhost", 
                                        username="root", 
                                        password="palmeranthony", 
                                        database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update materials set item=%s, model=%s, serial=%s, disc=%s, qty=%s, unit=%s where nameofbrand=%s",(                          
                                                                                                                                self.item.get(),
                                                                                                                                self.nameofbrand.get(),
                                                                                                                                self.model.get(),
                                                                                                                                self.serial.get(),
                                                                                                                                self.disc.get(),
                                                                                                                                self.qty.get(),
                                                                                                                                self.unit.get(),   
                                                                                                                            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Update", "Done")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="palmeranthony", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from materials")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.materials_table.delete(*self.materials_table.get_children())
            for i in rows:
                self.materials_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.materials_table.focus()
        content = self.materials_table.item(cursor_row)
        row = content["values"]
        self.item.set(row[0])
        self.nameofbrand.set(row[1])
        self.model.set(row[2])
        self.serial.set(row[3])
        self.disc.set(row[4])        
        self.qty.set(row[5])
        self.unit.set(row[6])

    def idelete(self):
        if self.item.get() == "" or self.nameofbrand.get() == "":
            messagebox.showerror("Error", "No blanks allowed")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="palmeranthony", database="Mydata")
            my_cursor=conn.cursor()
            query="delete from materials where nameofbrand=%s"
            value=(self.nameofbrand.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            self.fatch_data()
            messagebox.showinfo("Delete", "Deleted")

    # def sort_data(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="palmeranthony", database="Mydata")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("select * from materials order by item ASC")
    #     rows = my_cursor.fetchall()
    #     conn.commit()
    #     conn.close()
    #     # Clear the treeview
    #     for record in self.treeview.get_children():
    #         self.treeview.delete(record)
        
    #     # Re-insert the sorted data
    #     for row in rows:
    #         self.treeview.insert("", "end", values=row)
        



root = Tk()
ob = Materials(root)
root.mainloop()