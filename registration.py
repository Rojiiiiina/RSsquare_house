from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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

        # function decleration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "ALl fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password & conform password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree Our terms and condition")
        else:
            messagebox.showerror("Success", "welcome friends")
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()