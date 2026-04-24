from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class subjectClass:
    def __init__(self, root):  
        self.root = root
        self.root.title("Engineering College Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Hardcoded departments and semesters
        self.departments = ["Select Department",
            "Computer Science", "Mechanical Engineering", 
            "Civil Engineering", "Electrical Engineering", 
            "Electronics Engineering"
        ]
        self.semesters = ["Select Semester", "1", "2", "3", "4", "5", "6", "7", "8"]

        # Variables
        self.var_subject_id = StringVar()
        self.var_subject_code = StringVar()
        self.var_subject = StringVar() 
        self.var_credits = StringVar()
        self.var_professor = StringVar()
        self.var_semester = StringVar()
        self.var_duration = StringVar()
        self.var_department = StringVar()
        self.var_search = StringVar()

        # Title
        title = Label(self.root, text="Manage Subject Details", font=("goudy old style", 20, "bold"),
                      bg="#4B0082", fg="white").pack(side=TOP, fill=X)

        # Labels & Entries
        Label(self.root, text="Subject Code", font=("goudy old style", 15), bg='white').place(x=10, y=60)
        Label(self.root, text="Subject Name", font=("goudy old style", 15), bg='white').place(x=10, y=100)
        Label(self.root, text="Department", font=("goudy old style", 15), bg='white').place(x=10, y=140)
        Label(self.root, text="Credits", font=("goudy old style", 15), bg='white').place(x=10, y=180)
        Label(self.root, text="Professor", font=("goudy old style", 15), bg='white').place(x=10, y=220)
        Label(self.root, text="Semester", font=("goudy old style", 15), bg='white').place(x=10, y=260)
        Label(self.root, text="Duration", font=("goudy old style", 15), bg='white').place(x=10, y=300)

        Entry(self.root, textvariable=self.var_subject_code, font=("goudy old style", 15), bg='white').place(x=200, y=60, width=200)
        Entry(self.root, textvariable=self.var_subject, font=("goudy old style", 15), bg='white').place(x=200, y=100, width=200)
        self.department_combobox = ttk.Combobox(self.root, textvariable=self.var_department,
                                                values=self.departments, state="readonly", font=("goudy old style", 15))
        self.department_combobox.place(x=200, y=140, width=200)
        self.department_combobox.current(0)

        Entry(self.root, textvariable=self.var_credits, font=("goudy old style", 15), bg='white').place(x=200, y=180, width=200)
        Entry(self.root, textvariable=self.var_professor, font=("goudy old style", 15), bg='white').place(x=200, y=220, width=200)

        self.semester_combobox = ttk.Combobox(self.root, textvariable=self.var_semester,
                                              values=self.semesters, state="readonly", font=("goudy old style", 15))
        self.semester_combobox.place(x=200, y=260, width=200)
        self.semester_combobox.current(0)

        Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15), bg='white').place(x=200, y=300, width=200)

        # Buttons
        Button(self.root, text='Save', font=("goudy old style", 15), bg="#2196f3", fg="white", command=self.add).place(x=200, y=360, width=110, height=40)
        Button(self.root, text='Update', font=("goudy old style", 15), bg="#4caf50", fg="white", command=self.update).place(x=320, y=360, width=110, height=40)
        Button(self.root, text='Delete', font=("goudy old style", 15), bg="#f44336", fg="white", command=self.delete).place(x=440, y=360, width=110, height=40)
        Button(self.root, text='Clear', font=("goudy old style", 15), bg="#607d8b", fg="white", command=self.clear).place(x=560, y=360, width=110, height=40)

        # Search
        Label(self.root, text="Search By | Subject Name", font=("goudy old style", 15), bg='white').place(x=700, y=60)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg='lightyellow').place(x=950, y=60, width=200)
        Button(self.root, text='Search', font=("goudy old style", 15), bg="#03a9f4", fg="white", command=self.search).place(x=1160, y=60, width=100, height=28)

        # Table
        self.frame = Frame(self.root, bd=2, relief=RIDGE)
        self.frame.place(x=700, y=100, width=560, height=300)

        scrollx = Scrollbar(self.frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.frame, orient=VERTICAL)
        self.SubjectTable = ttk.Treeview(self.frame, columns=("subject_id", "subject_code", "name", "department", "credits", "professor", "semester", "duration"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SubjectTable.xview)
        scrolly.config(command=self.SubjectTable.yview)

        for col in self.SubjectTable["columns"]:
            self.SubjectTable.heading(col, text=col.capitalize())
            self.SubjectTable.column(col, width=100)
        self.SubjectTable["show"] = "headings"
        self.SubjectTable.pack(fill=BOTH, expand=1)
        self.SubjectTable.bind("<ButtonRelease-1>", self.get_data)

        self.create_table()
        self.show()

    def create_table(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS subject (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_code TEXT,
            name TEXT,
            department TEXT,
            credits TEXT,
            professor TEXT,
            semester TEXT,
            duration TEXT
        )""")
        con.commit()
        con.close()

    def add(self):
        if (self.var_subject_code.get() == "" or self.var_subject.get() == "" or
            self.var_department.get() == "Select Department" or self.var_semester.get() == "Select Semester"):
            messagebox.showerror("Error", "All fields (including Department & Semester) are required", parent=self.root)
            return

        if not self.var_credits.get().isdigit():
            messagebox.showerror("Error", "Credits must be a number", parent=self.root)
            return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("INSERT INTO subject (subject_code, name, department, credits, professor, semester, duration) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                self.var_subject_code.get(),
                self.var_subject.get(),
                self.var_department.get(),
                self.var_credits.get(),
                self.var_professor.get(),
                self.var_semester.get(),
                self.var_duration.get()
            ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Subject added successfully", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM subject")
        rows = cur.fetchall()
        self.SubjectTable.delete(*self.SubjectTable.get_children())
        for row in rows:
            self.SubjectTable.insert('', END, values=row)
        con.close()

    def get_data(self, ev):
        r = self.SubjectTable.focus()
        content = self.SubjectTable.item(r)
        row = content['values']
        if row:
            self.var_subject_id.set(row[0])
            self.var_subject_code.set(row[1])
            self.var_subject.set(row[2])
            self.var_department.set(row[3])
            self.var_credits.set(row[4])
            self.var_professor.set(row[5])
            self.var_semester.set(row[6])
            self.var_duration.set(row[7])

    def update(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("UPDATE subject SET subject_code=?, name=?, department=?, credits=?, professor=?, semester=?, duration=? WHERE subject_id=?", (
                self.var_subject_code.get(),
                self.var_subject.get(),
                self.var_department.get(),
                self.var_credits.get(),
                self.var_professor.get(),
                self.var_semester.get(),
                self.var_duration.get(),
                self.var_subject_id.get()
            ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Subject updated successfully", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def delete(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("DELETE FROM subject WHERE subject_id=?", (self.var_subject_id.get(),))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Subject deleted successfully", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_subject_id.set("")
        self.var_subject_code.set("")
        self.var_subject.set("")
        self.var_department.set(self.departments[0])
        self.var_credits.set("")
        self.var_professor.set("")
        self.var_semester.set(self.semesters[0])
        self.var_duration.set("")

    def search(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM subject WHERE name LIKE ?", ('%' + self.var_search.get() + '%',))
        rows = cur.fetchall()
        self.SubjectTable.delete(*self.SubjectTable.get_children())
        for row in rows:
            self.SubjectTable.insert('', END, values=row)
        con.close()

if __name__ == "__main__":
    root = Tk()
    obj = subjectClass(root)
    root.mainloop()
