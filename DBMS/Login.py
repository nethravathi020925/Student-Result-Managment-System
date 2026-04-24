import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        self.after_id = None

        # === Background Sections ===
        Label(self.root, bg="#08A3D2", bd=0).place(x=0, y=0, relheight=1, width=600)
        Label(self.root, bg="#031F3C", bd=0).place(x=600, y=0, relheight=1, relwidth=1)

        # === Login Frame ===
        login_frame = Frame(self.root, bg="white", bd=0, relief=RIDGE)
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("Segoe UI", 30, "bold"), bg="white", fg="#08A3D2")
        title.place(x=250, y=50)

        # === Email Input ===
        Label(login_frame, text="EMAIL ADDRESS", font=("Segoe UI", 16, "bold"), bg="white", fg="gray").place(x=250, y=120)
        self.txt_email = Entry(login_frame, font=("Segoe UI", 15), bg="#f1f1f1")
        self.txt_email.place(x=250, y=150, width=350, height=35)

        # === Password Input ===
        Label(login_frame, text="PASSWORD", font=("Segoe UI", 16, "bold"), bg="white", fg="gray").place(x=250, y=200)
        self.txt_pass_ = Entry(login_frame, show="*", font=("Segoe UI", 15), bg="#f1f1f1")
        self.txt_pass_.place(x=250, y=230, width=350, height=35)

        # === Links ===
        Button(login_frame, command=self.register_window, text="Register new Account?", font=("Segoe UI", 12, "underline"), bg="white", fg="#B00857", bd=0, cursor="hand2").place(x=250, y=280)
        Button(login_frame, command=self.forget_password_window, text="Forget Password?", font=("Segoe UI", 12, "underline"), bg="white", fg="#FF0000", bd=0, cursor="hand2").place(x=450, y=280)

        # === Login Button ===
        Button(login_frame, text="LOGIN", command=self.login, font=("Segoe UI", 18, "bold"), bg="#08A3D2", fg="white", activebackground="#026c95", activeforeground="white", cursor="hand2").place(x=250, y=330, width=350, height=45)

        # === Clock Display ===
        self.lbl = Label(self.root, text="Clock", font=("Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM, bg="white", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pass_.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect("rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=? AND question=? AND answer=?", (
                    self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Incorrect Security Question or Answer", parent=self.root2)
                else:
                    cur.execute("UPDATE users SET password=? WHERE email=?", (
                        self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Password reset successfully", parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter the email address", parent=self.root)
        else:
            try:
                con = sqlite3.connect("rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid email address", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    Label(self.root2, text="Forget Password", font=("Segoe UI", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

                    Label(self.root2, text="Security Question", font=("Segoe UI", 14, "bold"), bg="white", fg="gray").place(x=50, y=80)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("Segoe UI", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=50, y=110, width=250)
                    self.cmb_quest.current(0)

                    Label(self.root2, text="Answer", font=("Segoe UI", 14, "bold"), bg="white", fg="gray").place(x=50, y=150)
                    self.txt_answer = Entry(self.root2, font=("Segoe UI", 13), bg="#f1f1f1")
                    self.txt_answer.place(x=50, y=180, width=250)

                    Label(self.root2, text="New Password", font=("Segoe UI", 14, "bold"), bg="white", fg="gray").place(x=50, y=220)
                    self.txt_new_pass = Entry(self.root2, font=("Segoe UI", 13), bg="#f1f1f1")
                    self.txt_new_pass.place(x=50, y=250, width=250)

                    Button(self.root2, text="Reset Password", command=self.forget_password, bg="#08A3D2", fg="white", font=("Segoe UI", 13, "bold"), cursor="hand2").place(x=100, y=310)
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def register_window(self):
        if self.after_id:
          self.lbl.after_cancel(self.after_id)
        
        self.root.destroy()
        from Register import Register

    def login(self):

        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect("rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=? AND password=?", (
                    self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid EMAIL or PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome {row[1]}", parent=self.root)
                    role = row[4]
                    self.root.withdraw()
                    new_root = Toplevel(self.root)
                    if role == 'Admin':
                        from Dashboard import RMS
                        RMS(new_root)
                    elif role == 'Student':
                        from StudentDashboard import StudentDashboard
                        # StudentDashboard(new_root)
                        cur.execute("SELECT roll FROM student WHERE email=?", (self.txt_email.get(),))
                        student_data = cur.fetchone()

                        if student_data:
                            student_roll = student_data[0]
                            StudentDashboard(new_root, student_roll=student_roll)
                        else:
                            messagebox.showerror("Error", "Student record not found for this email.", parent=self.root)
                            new_root.destroy()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #---------- For Clock Image ------------
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300))
        clock.paste(bg,(50,50))

        #---------- Hour Line Image ---------------
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #---------- Min Line Image --------------
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #---------- Sec Line Image --------------
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        # if not self.is_running:
        #  return
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.after_id = self.lbl.after(200, self.working)

    # def stop_clock(self):
    #  self.is_running = False
    #  if self.after_id:
    #     try:
    #         self.lbl.after_cancel(self.after_id)
    #     except Exception:
    #         pass



        

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    # root.protocol("WM_DELETE_WINDOW", obj.stop_clock)  # This stops the clock cleanly
    root.mainloop()
