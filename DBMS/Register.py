from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow
import sqlite3
import re


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="white")

        # =====Register Frame====
        frame1 = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame1.place(x=480, y=100, width=700, height=550)

        title = Label(frame1, text="Register Here", font=("Helvetica", 22, "bold"), bg="white", fg="#333")
        title.place(x=50, y=20)

        # =====Row1=====
        f_name = Label(frame1, text="First Name", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        f_name.place(x=50, y=80)
        self.txt_fname = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0")
        self.txt_fname.place(x=50, y=110, width=250)

        l_name = Label(frame1, text="Last Name", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        l_name.place(x=370, y=80)
        self.txt_lname = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0")
        self.txt_lname.place(x=370, y=110, width=250)

        # =====Row2=====
        contact = Label(frame1, text="Contact No", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        contact.place(x=50, y=150)
        self.txt_contact = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0")
        self.txt_contact.place(x=50, y=180, width=250)

        email = Label(frame1, text="Email", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        email.place(x=370, y=150)
        self.txt_email = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0")
        self.txt_email.place(x=370, y=180, width=250)

        # =====Row3=====
        role_label = Label(frame1, text="Role", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        role_label.place(x=50, y=220)
        self.cmb_role = ttk.Combobox(frame1, font=("Helvetica", 13), state='readonly', justify=CENTER)
        self.cmb_role['values'] = ("Select", "Admin", "Student")
        self.cmb_role.place(x=50, y=250, width=250)
        self.cmb_role.current(0)

        question = Label(frame1, text="Security Question", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        question.place(x=370, y=220)
        self.cmb_quest = ttk.Combobox(frame1, font=("Helvetica", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=370, y=250, width=250)
        self.cmb_quest.current(0)

        # =====Row4=====
        answer = Label(frame1, text="Answer", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        answer.place(x=50, y=290)
        self.txt_answer = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0")
        self.txt_answer.place(x=50, y=320, width=250)

        password = Label(frame1, text="Password", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        password.place(x=370, y=290)
        self.txt_password = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0", show="*")
        self.txt_password.place(x=370, y=320, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("Helvetica", 15, "bold"), bg="white", fg="#555")
        cpassword.place(x=50, y=360)
        self.txt_cpassword = Entry(frame1, font=("Helvetica", 14), bg="#f0f0f0", show="*")
        self.txt_cpassword.place(x=50, y=390, width=250)

        # =====Terms & Register=====
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree to the Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("Helvetica", 11))
        chk.place(x=50, y=430)

        # btn_register = Button(frame1, text="Register", font=("Helvetica", 15, "bold"), bg="#28a745", fg="white", command=self.register_data, cursor="hand2")
        # btn_register.place(x=50, y=470, width=150, height=40)
     
        # or_label = Label(frame1, text="or", font=("Helvetica", 13, "bold"), bg="white", fg="#555")
        # or_label.place(x=210, y=480)

        # btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("Helvetica", 16), bd=0, fg="blue", bg="white", cursor="hand2")
        # btn_login.place(x=250, y=470, width=100,height=40)

        # ===== Buttons in a sub-frame =====
        btn_frame = Frame(frame1, bg="white")
        btn_frame.place(x=50, y=470)  # adjust X to center

        # Register Button
        btn_register = Button(btn_frame, text="Register", font=("Helvetica", 14, "bold"), bg="#28a745", fg="white", command=self.register_data, cursor="hand2")
        btn_register.grid(row=0, column=0, padx=5)

        # 'or' Label
        or_label = Label(btn_frame, text="or", font=("Helvetica", 13, "bold"), bg="white", fg="#555")
        or_label.grid(row=0, column=1, padx=5)

        # Sign In Button
        btn_login = Button(btn_frame, text="Sign In", command=self.login_window, font=("Helvetica", 14, "bold"), bd=0, fg="white", bg="blue", cursor="hand2")
        btn_login.grid(row=0, column=2, padx=5)


    def login_window(self):
       self.root.destroy()  # Close the register window
       import Login
       from Login import Login_window  
       root = Tk()
       Login_window(root)
       root.mainloop()

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
        self.cmb_role.current(0)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "" or self.cmb_role.get() == "Select":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.txt_email.get()):
            messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password Should be SAME", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree to Our Terms and Conditions", parent=self.root)
        elif not re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', self.txt_password.get()):
            messagebox.showerror("Error", "Password must be at least 8 characters long and include letters, numbers, and a special character.", parent=self.root)
        else:
            try:
                con = sqlite3.connect("rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User Already Exists, Please try another email", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO users (f_name, l_name, contact, email, role, question, answer, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(),
                         self.txt_email.get(), self.cmb_role.get(), self.cmb_quest.get(), self.txt_answer.get(), self.txt_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()
