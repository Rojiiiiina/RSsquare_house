from tkinter import *
# from typing_extensions import Self
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsHouse:
    def __init__(self, root):
        self.root = root
        self.root.title("RSsquare House")
        self.root.geometry("1150x600+280+120")

        # title
        lbl_title = Label(self.root, text="House Booking", font=("times new roman", 18, "bold"), bg="black", fg="light blue",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1150, height=50)

        # logo
        img2 = Image.open(r"C:\Users\hp\Pictures\New folder\logo.png")
        img2 = img2.resize((100, 40), Image.HOUSE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        #     # labelframe
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New House Add",
                                    font=("times new roman", 12, "bold"), padx=2, )
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # area
        lbl_area = Label(labelframeleft, text="Area", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_area.grid(row=0, column=0, sticky=W)

        self.var_area = StringVar()
        entry_area = ttk.Entry(labelframeleft, textvariable=self.var_area, width=20, font=("arial", 13, "bold"))
        entry_area.grid(row=0, column=1, sticky=W)



        # Housetype
        lbl_HouseType = Label(labelframeleft, text="House Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_HouseType.grid(row=2, column=0, sticky=W)
        self.var_HouseType = StringVar()
        entry_HouseType = ttk.Entry(labelframeleft, textvariable=self.var_HouseType, width=20, font=("arial", 13, "bold"))
        entry_HouseType.grid(row=2, column=1, sticky=W)

        # btn
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold",
                        width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 12, "bold"), bg="black",
                          fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        #  table form search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show House Details",
                                 font=("times new roman", 12, "bold"), padx=2, )
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.house_view = ttk.Treeview(Table_Frame, column=("area", "housetype"), xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.house_view.xview)
        scroll_y.config(command=self.house_view.yview)

        self.house_view.heading("area", text="Area")
        self.house_view.heading("housetype", text="House Type")

        self.house_view["show"] = "headings"

        self.house_view.column("area", width=100)
        self.house_view.column("housetype", width=100)

        self.house_view.pack(fill=BOTH, expand=1)
        self.house_view.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # add data
    def add_data(self):
        if self.var_area.get() == "" or self.var_HouseType.get() == "":
            messagebox.showerror("Error", "ALL Fields Are Required")

        else:
            try:
                conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12", database="housing")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_area.get(),
                    self.var_HouseType.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

            #  fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2002", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.house_view.delete(*self.house_view.get_children())
            for i in rows:
                self.house_view.insert("", END, values=i)
                conn.commit()
            conn.close()

    #  get cursor
    def get_cursor(self, event=""):
        cursor_row = self.house_view.focus()
        content = self.house_view.item(cursor_row)
        row = content["value"]

        self.var_area.set(row[0]),
        self.var_HouseType.set(row[1])

        #  update function

    def update(self):
        if self.var_area.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12", database="housing")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Area=%a,HouseType=%a"(
                self.var_area.get(),
                self.var_HouseType.get(),

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "New House detail has been update successfully", parent=self.root)

            # delete function

    def mDelete(self):
        mDelete = messagebox.askyesno("RSsquare House", "Do you want to delete this House Details",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(owner="ownerhere", username="sweethome", password="p@ssword12", database="housing")
            my_cursor = conn.cursor()
            query = "delete from details where Housetype=%a"
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_area.set(""),
        self.var_HouseType.set("")


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()