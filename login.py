from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # self.bg=ImageTk.PhotoImage(file=r"C:\Users\Acer\OneDrive\New folder\bg.png")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=150, width=350, height=450)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # labels
        username = lbl = Label(frame, text="username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=140)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=20, y=170, width=270)

        password = lbl = Label(frame, text="password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=210)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=20, y=250, width=270)

        # login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=120, y=300, width=70, height=30)

        # registerbutton
        registerbtn = Button(frame, text="New User Register", command=self.rigister_window,
                             font=("times new roman", 15, "bold"), borderwidth=0, fg="white", bg="black",
                             activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=330, width=160)

        # forgetpassword button
        registerbtn = Button(frame, text="Forget Password", font=("times new roman", 15, "bold"), borderwidth=0,
                             fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=8, y=360, width=160)

    def rigister_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "sonu" and self.txtpass.get() == "ashi":
            messagebox.showinfo("Success", "Welcome to hotel")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROJINAMISHRA",
                                           database="realestate")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s,"(
                self.var_email.get(),
                self.var_pass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & password")
            else:
                open_main = messagebox.askyesno("yesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.new_window)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # varible
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # bg image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Acer\Pictures\New folder\2690573.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Acer\Pictures\New folder\photo-1596386461350-326ccb383e9f.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=70, width=400, height=500)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=420, y=70, width=800, height=500)

        register_lbl = Label(frame, text="REGISTER HERE", font=("timews new roman", 20, "bold"), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=20, y=20)

        # label and entry
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # row2
        contact = Label(frame, text="Contact no", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # row3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Favourite Game")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # row 4

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        email = Label(frame, text="Conform Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=310)

        self.txt_conform = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_conform.place(x=370, y=340, width=250)

        # check button
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, text="I Agree The Terms & Conditions", font=("times new roman", 10, "bold"),
                                    onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        #  button
        img = Image.open(r"C:\Users\Acer\Pictures\New folder\download.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Acer\Pictures\New folder\download (1).jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)

    # function decleration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "ALl fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "passwor & conform password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree Our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="2002", database="mydata")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_SecurityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")
if __name__ == "__main__":
    main()