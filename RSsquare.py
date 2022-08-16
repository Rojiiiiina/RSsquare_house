from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from house import Housebooking
from detail import DetailsHouse


class RSsquareHouse:
    def __init__(self, root):
        self.root = root
        self.root.title("RSsquare House")
        self.root.geometry("1650x750+0+0")

        # 1st img
        img1 = Image.open(r"C:\Users\hp\Pictures\New folder\download12.jpg")
        img1 = img1.resize((1550, 140), Image.House)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # 2nd image
        img2 = Image.open(r"C:\Users\hp\Pictures\New folder\logo.png")
        img2 = img2.resize((230, 140), Image.House)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # Title

        lbl_title = Label(self.root, text="RSsquare House", font=("times new roman", 40, "bold"), bg="black",
                          fg="light blue", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # frame

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # menu

        lbl_menu = Label(self.root, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,
                         relief=RIDGE)
        lbl_menu.place(x=0, y=195, width=230)

        # frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=225, height=160)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22,
                          font=("times new roman", 13, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        house_btn = Button(btn_frame, text="HOUSE", command=self.housebooking, width=22,
                          font=("times new roman", 13, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        house_btn.grid(row=1, column=0, pady=1)

        detail_btn = Button(btn_frame, text="DETAIL", command=self.details_house, width=22,
                            font=("times new roman", 13, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        detail_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 13, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 13, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def housebooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Housebooking(self.new_window)

    def details_house(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsHouse(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = RSsquareHouse(root)
    root.mainloop()