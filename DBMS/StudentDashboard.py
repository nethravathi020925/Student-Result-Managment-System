from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from Report import reportClass
import sqlite3
from fpdf import FPDF

class StudentDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Dashboard - Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#F3E9F9")

        # === Set current logged-in student roll number ===
        # You should ideally fetch this dynamically after login
        self.student_roll = 1  # <--- Replace this with the actual logged-in student's roll

        # Logo
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        title = Label(self.root, text="Welcome Student", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("goudy old style", 20, "bold"),
                      bg="#4B0082", fg="white")
        title.pack(side=TOP,fill=X)

        # Menu Frame
        M_Frame = LabelFrame(self.root, text="Menu", font=("times new roman", 15), bg="white")
        M_Frame.pack(side=TOP, fill=X, padx=10,pady=10)

        #---------- content window ----------------
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((1350,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(relx=0.5, y=180, anchor='n',width=1350,height=350)

        Button(M_Frame, text="View Results", font=("goudy old style", 15, "bold"), bg="#8E44AD", fg="white",
               cursor="hand2", command=self.view_report,width=32).pack(side=LEFT, padx=5, pady=5, ipadx=10, ipady=8)

        Button(M_Frame, text="Download Report", font=("goudy old style", 15, "bold"), bg="#228B22", fg="white",
               cursor="hand2", command=self.download_report,width=32).pack(side=LEFT, padx=5, pady=5, ipadx=10, ipady=8)

        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#8B0000", fg="white",
               cursor="hand2",width=32,command=self.logout).pack(side=LEFT, padx=5, pady=5, ipadx=10, ipady=8)

        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#6a040f", fg="white",
               cursor="hand2", command=self.root.quit,width=32).pack(side=LEFT, padx=5, pady=5, ipadx=10, ipady=8)

        # Info (Optional Placeholder)
        self.lbl_welcome = Label(self.root, text="Logged in as: Student", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_welcome.place(x=500, y=600, width=550, height=100)

        # Footer
        footer = Label(self.root, text="Engineering SRMS\nContact: 987xxxxx01",
                       font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def view_report(self):
        self.new_win = Toplevel(self.root)
        self.new_report = reportClass(self.new_win)

    def logout(self):
        
        self.root.destroy()
        from Login import Login_window
        root = Tk()
        obj = Login_window(root)
        root.mainloop()

    def download_report(self):
        def get_grade(percentage):
            if percentage >= 90:
                return "O"
            elif percentage >= 80:
                return "A+"
            elif percentage >= 70:
                return "A"
            elif percentage >= 60:
                return "B+"
            elif percentage >= 55:
                return "B"
            elif percentage >= 50:
                return "C"
            elif percentage >=40:
                return "P"
            else:
                return "F"

        try:
            roll_no = simpledialog.askinteger("Input", "Enter student roll number:", parent=self.root)
            if roll_no is None:
                return

            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            cur.execute("SELECT name, department, semester FROM student WHERE roll=?", (roll_no,))
            student = cur.fetchone()
            if student is None:
                messagebox.showerror("Error", f"Student record not found for roll number {roll_no}")
                return
            name, department, semester = student

            cur.execute("SELECT subject, marks_ob, full_marks, per FROM result WHERE roll=?", (roll_no,))
            results = cur.fetchall()
            if not results:
                messagebox.showinfo("No Data", f"No results found for roll number {roll_no}.")
                return

            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Title
            pdf.set_font("Arial", 'B', 18)
            pdf.cell(0, 10, "Student Result Report", ln=True, align='C')
            pdf.ln(10)

            # Student info
            pdf.set_font("Arial", '', 12)
            pdf.cell(50, 8, "Name:", 0)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, name, ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.cell(50, 8, "Roll No:", 0)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, str(roll_no), ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.cell(50, 8, "Department:", 0)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, department, ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.cell(50, 8, "Semester:", 0)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, str(semester), ln=True)
            pdf.ln(10)

            # Table headers including Grade
            pdf.set_fill_color(100, 100, 255)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(50, 10, "Subject", border=1, fill=True, align='C')
            pdf.cell(30, 10, "Marks Obt.", border=1, fill=True, align='C')
            pdf.cell(30, 10, "Full Marks", border=1, fill=True, align='C')
            pdf.cell(40, 10, "Percentage", border=1, fill=True, align='C')
            pdf.cell(30, 10, "Grade", border=1, fill=True, align='C')
            pdf.ln()

            pdf.set_fill_color(240, 240, 240)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Arial", '', 12)
            fill = False

            total_marks_obtained = 0
            total_full_marks = 0

            for subject, marks_ob, full_marks, per in results:
                grade = get_grade(per)
                total_marks_obtained += marks_ob
                total_full_marks += full_marks

                pdf.cell(50, 10, subject, border=1, fill=fill)
                pdf.cell(30, 10, str(marks_ob), border=1, fill=fill, align='C')
                pdf.cell(30, 10, str(full_marks), border=1, fill=fill, align='C')
                pdf.cell(40, 10, f"{per:.2f}%", border=1, fill=fill, align='C')
                pdf.cell(30, 10, grade, border=1, fill=fill, align='C')
                pdf.ln()
                fill = not fill

            # Calculate overall percentage and grade
            if total_full_marks > 0:
                overall_percentage = (total_marks_obtained / total_full_marks) * 100
                overall_grade = get_grade(overall_percentage)
            else:
                overall_percentage = 0
                overall_grade = "N/A"

            pdf.ln(10)
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, f"Total Marks Obtained: {total_marks_obtained} / {total_full_marks}", ln=True)
            pdf.cell(0, 10, f"Overall Percentage: {overall_percentage:.2f}%", ln=True)
            pdf.cell(0, 10, f"Overall Grade: {overall_grade}", ln=True)

            filename = f"{roll_no}_result.pdf"
            pdf.output(filename)

            messagebox.showinfo("Success", f"Report downloaded as '{filename}'")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        import os
        print("Saved to:", os.getcwd())



if __name__ == "__main__":
    root = Tk()
    obj = StudentDashboard(root)
    root.mainloop()
