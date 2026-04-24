from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("College Student Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="View Student Results", font=("goudy old style", 20, "bold"), bg="#4B0082", fg="white")
        title.place(x=10, y=15, width=1180, height=50)

        self.var_search = StringVar()

        lbl_search = Label(self.root, text="Search by Roll No", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_search.place(x=300, y=100)

        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg='lightyellow')
        txt_search.place(x=450, y=100, width=180)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=640, y=100, width=100, height=28)

        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=750, y=100, width=100, height=28)

        # === Treeview ===
        self.tree = ttk.Treeview(self.root, columns=("subject", "marks", "full", "percentage","grade"), show="headings")
        self.tree.place(x=50, y=150, width=1100, height=250)
        self.tree.heading("subject", text="Subject")
        self.tree.heading("marks", text="Marks Obtained")
        self.tree.heading("full", text="Full Marks")
        self.tree.heading("percentage", text="Percentage")
        self.tree.heading("grade" , text="Grade")

        self.tree.column("subject", width=300)
        self.tree.column("marks", width=200)
        self.tree.column("full", width=200)
        self.tree.column("percentage", width=200)
        self.tree.column("grade" , width=150)

        # === Summary Labels ===
        self.total_marks_var = StringVar()
        self.full_marks_var = StringVar()
        self.percentage_var = StringVar()

        lbl_total = Label(self.root, text="Total Marks:", font=("goudy old style", 15), bg='white')
        lbl_total.place(x=250, y=420)
        lbl_total_val = Label(self.root, textvariable=self.total_marks_var, font=("goudy old style", 15, 'bold'), bg='lightyellow', width=10)
        lbl_total_val.place(x=370, y=420)

        lbl_full = Label(self.root, text="Full Marks:", font=("goudy old style", 15), bg='white')
        lbl_full.place(x=500, y=420)
        lbl_full_val = Label(self.root, textvariable=self.full_marks_var, font=("goudy old style", 15, 'bold'), bg='lightyellow', width=10)
        lbl_full_val.place(x=610, y=420)

        lbl_percent = Label(self.root, text="Overall %:", font=("goudy old style", 15), bg='white')
        lbl_percent.place(x=740, y=420)
        lbl_percent_val = Label(self.root, textvariable=self.percentage_var, font=("goudy old style", 15, 'bold'), bg='lightyellow', width=10)
        lbl_percent_val.place(x=850, y=420)


    
    def calculate_grade(self, percent):
        percent = float(percent)
        if percent >= 90:
            return "O"
        elif percent >= 80:
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


    def search(self):
        roll = self.var_search.get().strip()
        if roll == "":
            messagebox.showerror("Error", "Roll No should be provided", parent=self.root)
            return
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("SELECT subject, marks_ob, full_marks FROM result WHERE roll=?", (roll,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Error", "No results found", parent=self.root)
                return

            self.tree.delete(*self.tree.get_children())  # Clear table
            total_marks = 0
            total_full_marks = 0

            for row in rows:
                subject, marks, fmarks = row
                percent = (int(marks) / int(fmarks)) * 100
                grade = self.calculate_grade(percent)
                self.tree.insert("", END, values=(subject, marks, fmarks, f"{percent:.2f}%", grade))
                total_marks += int(marks)
                total_full_marks += int(fmarks)

            overall_percent = (total_marks / total_full_marks) * 100 if total_full_marks != 0 else 0
            self.total_marks_var.set(str(total_marks))
            self.full_marks_var.set(str(total_full_marks))
            self.percentage_var.set(f"{overall_percent:.2f}%")

        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_search.set("")
        self.tree.delete(*self.tree.get_children())
        self.total_marks_var.set("")
        self.full_marks_var.set("")
        self.percentage_var.set("")


if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
