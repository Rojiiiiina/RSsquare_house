from tkinter import *
# from typing_extensions import Self
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class housebooking:
    def __init__(self, root):
        self.root = root
        self.root.title("RSsquare House")
        self.root.geometry("1050x550+220+100")

        # variables
        self.var_contact = StringVar()
        self.var_bookeddate = StringVar()
        self.var_housetype = StringVar()
        self.var_houseavailable = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        #     # title
        lbl_title = Label(self.root, text="HOUSE BOOKING", font=("times new roman", 18, "bold"), bg="black", fg="gold",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1150, height=50)

        #     # logo
        img2 = Image.open(r"C:\Users\hp\Pictures\New folder\logo.png")
        img2 = img2.resize((100, 40), Image.House)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        #     # labelframe
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Housebooking Details",
                                    font=("times new roman", 12, "bold"), padx=2, )
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # customer contact

        lbl_cust_contact = Label(labelframeleft, text="Customer contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # fetch data button
        btnFetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 9, "bold"),
                              bg="black", fg="gold", width=8)
        btnFetchData.place(x=340, y=4)

        # #    booked date
        booked_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Check_in Date:", padx=2, pady=6)
        booked_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_bookeddate, width=29,
                                     font=("arial", 13, "bold"), )
        txtbooked_date.grid(row=1, column=1)

        # #     # house type
        label_houseType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_houseType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                       database="housing")
        my_cursor = conn.cursor()
        my_cursor.execute("select HouseType from details")
        ide = my_cursor.fetchall()

        combo_houseType = ttk.Combobox(labelframeleft, textvariable=self.var_housetype, font=("arial", 12, "bold"),
                                       width=27, state="readonly")
        combo_houseType["value"] = ide
        combo_houseType.current(0)
        combo_houseType.grid(row=3, column=1)

        # #     # Available house
        lblHouseAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Available house:", padx=2, pady=6)
        lblHouseAvailable.grid(row=4, column=0, sticky=W)
        # txtHouseAvailable=ttk.Entry(labelframeleft,textvariable=self.var_houseavailable,width=29,font=("arial",13,"bold"))
        # txtHouseAvailable.grid(row=4,column=1)

        # #     # paid tax
        lblAreaOfHouse = Label(labelframeleft, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblAreaOfHouse.grid(row=7, column=0, sticky=W)
        txtAreaOfHouse = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width=29, font=("arial", 13, "bold"))
        txtAreaOfHouse.grid(row=7, column=1)

        # #     # sub total
        lblAreaOfHouse = Label(labelframeleft, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblAreaOfHouse.grid(row=8, column=0, sticky=W)
        txtAreaOfHouse = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, width=29,
                                   font=("arial", 13, "bold"))
        txtAreaOfHouse.grid(row=8, column=1)

        # total cost
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_total, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # btn
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # bill button

        btnBill = Button(labelframeleft, text="Bill", command=self.total, font=("arial", 12, "bold"), bg="black",
                         fg="gold", width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # btn
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold",
                        width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black",
                          fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # table frame and search system
        Table_frameUp = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search House",
                                   font=("times new roman", 12, "bold"), padx=2, )
        Table_frameUp.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_frameUp, font=("arial", 12, "bold"), text="Search by:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_frameUp, textvariable=self.search_var, font=("arial", 12, "bold"), width=15,
                                    state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(Table_frameUp, textvariable=self.txt_search, width=24, font=("arial", 10, "bold"))
        txtsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(Table_frameUp, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=9)
        btnsearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_frameUp, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # show data table
        details_table = Frame(Table_frameUp, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.house_table = ttk.Treeview(details_table, column=(
            "contact", "bookeddate", "housetype", "houseavailable", "mobile"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.house_table.xview)
        scroll_y.config(command=self.house_table.yview)

        self.house_table.heading("contact", text="Contact")
        self.house_table.heading("Bookeddate", text="Booked_date")
        self.house_table.heading("housetype", text="House Type")
        self.house_table.heading("houseavailable", text="House No")

        self.house_table["show"] = "headings"
        self.house_table.column("contact", width=100)
        self.house_table.column("bookeddate", width=100)
        self.house_table.column("roomtype", width=100)
        self.house_table.column("roomavailable", width=100)

        self.house_table.pack(fill=BOTH, expand=1)

        self.house_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # add data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_bookeddate.get() == "":
            messagebox.showerror("Error", "ALL Fields Are Required")

        else:
            try:
                conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                               database="housing")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into house values(%a,%a,%a,%a,%a,%a,%a,)", (
                    self.var_contact.get(),
                    self.var_bookeddate.get(),
                    self.var_housetype.get(),
                    self.var_houseavailable.get(),

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "House Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                       database="housing")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.house_table.delete(self.house_table.get_children())
            for i in rows:
                self.house_table.insert("", END, values=i)
                conn.commit()
            conn.close()

    #  get cursor
    def get_cursor(self, event=""):
        cursor_row = self.house_table.focus()
        content = self.house_table.item(cursor_row)
        row = content["value"]

        self.var_contact.set(row[0])
        self.var_bookeddate.set(row[1])
        self.var_housetype.set(row[2])
        self.var_houseavailable.set(row[3])

    #  update function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update house set bookeddate=%a,check_out=%a,housetype=%a,houseavailable=%a,  where Contact=%a",
                (
                    self.var_contact.get(),
                    self.var_bookeddate.get(),
                    self.var_housetype.get(),
                    self.var_houseavailable.get(),

                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "House detail has been update successfully", parent=self.root)

            # delete function

    def mDelete(self):
        mDelete = messagebox.askyesno("RSsquare", "Do you want to delete this customer",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            query = "delete from customer where Contact=%a"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

        # reset function

    def reset(self):
        self.var_contact.set("")
        self.var_bookeddate.set("")
        self.var_housetype.set("")
        self.var_houseavailable.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        # all data fetch

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        else:
            # name
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            query = ("select Name from customer where mobile=%a")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

            #  gender
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            query = ("select Gender from customer where mobile=%a")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblName = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=30)

            lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl.place(x=90, y=30)
            # email
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            query = ("select Email from customer where mobile=%a")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblName = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=60)

            lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl.place(x=90, y=60)

            #  nationality
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            query = ("select Nationality from customer where mobile=%a")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblName = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=90)

            lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl.place(x=90, y=90)

            #  address
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                           database="housing")
            my_cursor = conn.cursor()
            query = ("select Address from customer where mobile=%a")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblName = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=120)

            lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl.place(x=90, y=120)

    # search system
    def search(self):
        conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12",
                                       database="housing")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where" + str(self.search_var.get()) + "LIKE'%'" + str(
            self.txt_search.get()) + "'%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.house_table.delete(*self.house_table.get_children())
            for i in rows:
                self.house_table.insert("", END, values=i)
                conn.commit()
                conn.close()

    def total(self):
        bookeddate = self.var_bookeddate.get()
        bookeddate = datetime.strptime(bookeddate, "%d/%m/%Y")


if __name__ == "__main__":
    root = Tk()
    obj = Housebooking(root)
    root.mainloop()