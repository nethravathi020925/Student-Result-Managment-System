from tkinter import *
import sqlite3
from tkinter import ttk,messagebox
from PIL import Image, ImageTk,ImageDraw
from Subject import subjectClass
from Student import studentClass
from Result import resultClass
from Report import reportClass
from tkinter.colorchooser import askcolor
from datetime import *
from math import *

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#F3E9F9")

        # === Logo ===
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # === Title ===
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("Times New Roman", 20, "bold"), bg="#4B0082", fg="white")
        title.place(x=0, y=0, relwidth=1, height=60)

        # === Menu Frame (Full Width) ===
        M_Frame = Frame(self.root, bg="white")
        M_Frame.place(x=0, y=60, relwidth=1, height=90)

        # === Button Style and Placement ===
        self.create_menu_button(M_Frame, "Add Subjects", "#8E44AD", command=self.add_subject)
        self.create_menu_button(M_Frame, "Add Students", "#8E44AD", command=self.add_student)
        self.create_menu_button(M_Frame, "Add Results", "#8E44AD", command=self.add_result)
        self.create_menu_button(M_Frame, "View Results", "#8E44AD", command=self.add_report)
        self.create_menu_button(M_Frame, "Logout", "#a4161a", command=self.logout)
        self.create_menu_button(M_Frame, "Exit", "#6a040f", command=self.root.quit)


        #---------- content window ----------------
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,320))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        # Example: Dynamically center at any window size
        window_width = 1350
        img_width = 920
        x_pos = (window_width - img_width) // 2  # center horizontally

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=x_pos, y=180, width=1500, height=350)

       #  self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)
        # === Dashboard Info Boxes ===
        self.lbl_subject = Label(self.root, text="Total Subjects\n[ 0]", font=("Segoe UI", 20, "bold"), bd=10,
                                 relief=RIDGE, bg="#e43b06", fg="white", justify=CENTER)
        self.lbl_subject.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0]", font=("Segoe UI", 20, "bold"), bd=10,
                                 relief=RIDGE, bg="#0676ad", fg="white", justify=CENTER)
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0]", font=("Segoe UI", 20, "bold"), bd=10,
                                relief=RIDGE, bg="#038074", fg="white", justify=CENTER)
        self.lbl_result.place(x=1020, y=530, width=300, height=100)


        #----------- clock -------------
        self.lbl=Label(self.root,text="\nClock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,height=450,width=350)
        self.working_after_id = None
        self.update_after_id = None

        self.working()
        self.update_details()

         # === Footer ===
        footer = Label(self.root, text="SRMS\nContact: 987xxxxx01",
                       font=("Segoe UI", 12), bg="#262626", fg="white", pady=6)
        footer.pack(side=BOTTOM, fill=X)


    def create_menu_button(self, parent, text, color, command=None):
        btn = Button(parent, text=text, font=("Segoe UI", 14, "bold"), bg=color, fg="white",
                     activebackground="#222", activeforeground="white", cursor="hand2", command=command)
       #  btn.place(x=x, y=20, width=200, height=40)

        btn.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=10)

        def on_enter(e): btn['bg'] = '#732d91'
        def on_leave(e): btn['bg'] = color
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def add_subject(self):
        self.new_win = Toplevel(self.root)
        self.new_subject = subjectClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_student = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_result = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_report = reportClass(self.new_win)

    def logout(self):
        if self.working_after_id is not None:
            self.lbl.after_cancel(self.working_after_id)
            self.working_after_id = None

        if self.update_after_id is not None:
            self.root.after_cancel(self.update_after_id)
            self.update_after_id = None

        self.root.destroy()
        from Login import Login_window
        root = Tk()
        obj = Login_window(root)
        root.mainloop()

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
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.working_after_id = self.lbl.after(200,self.working)

    def update_details(self):
       
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from subject")
            cr=cur.fetchall()
            self.lbl_subject.config(text=f"Total Subjects\n[{str(len(cr))}]")

            cur.execute("select * from student")
            st=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(st))}]")

            cur.execute("select * from result")
            rs=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(rs))}]")

            self.update_after_id = self.root.after(2000, self.update_details)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
