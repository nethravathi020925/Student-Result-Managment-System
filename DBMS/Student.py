from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Engineering College - Student Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#4B0082", fg="white")
        title.pack(side=TOP, fill=X)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_department = StringVar()
        self.var_semester = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_address = StringVar()
        self.var_search = StringVar()

        # Labels
        Label(self.root, text="Roll No", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=60)
        Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=100)
        Label(self.root, text="Email", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        Label(self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=180)
        Label(self.root, text="D.O.B", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=220)
        Label(self.root, text="Contact", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=260)
        Label(self.root, text="Department", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=300)
        Label(self.root, text="Semester", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=340)
        Label(self.root, text="State", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=380)
        Label(self.root, text="City", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=60)
        Label(self.root, text="Pin", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=100)
        Label(self.root, text="Address", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=140)

        # Entries
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg='white')
        self.txt_roll.place(x=150, y=60, width=200)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg='white')
        self.txt_name.place(x=150, y=100, width=200)

        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg='white')
        self.txt_email.place(x=150, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Others"), font=("goudy old style", 15), state="readonly")
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg='white')
        self.txt_dob.place(x=150, y=220, width=200)

        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg='white')
        self.txt_contact.place(x=150, y=260, width=200)

        self.txt_department = ttk.Combobox(self.root, textvariable=self.var_department, values=("Select Department",
            "Computer Science", "Mechanical Engineering", 
            "Civil Engineering", "Electrical Engineering", 
            "Electronics Engineering"), font=("goudy old style", 15), state="readonly")
        self.txt_department.place(x=150, y=300, width=200)
        self.txt_department.current(0)

        self.txt_semester = ttk.Combobox(self.root, textvariable=self.var_semester, values=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8"), font=("goudy old style", 15), state="readonly")
        self.txt_semester.place(x=150, y=340, width=200)
        self.txt_semester.current(0)

        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg='white')
        self.txt_state.place(x=150, y=380, width=200)

        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15), bg='white')
        self.txt_city.place(x=480, y=60, width=200)

        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg='white')
        self.txt_pin.place(x=480, y=100, width=200)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg='white', height=4, width=22)
        self.txt_address.place(x=480, y=140)

        # Subject Button & Listbox
        # Button(self.root, text='Fetch Subjects', font=("goudy old style", 12, "bold"), bg="#009688", fg="white", command=self.fetch_subjects).place(x=370, y=380, width=140, height=30)
        # self.subject_listbox = Listbox(self.root, font=("goudy old style", 13), selectmode=MULTIPLE)
        # self.subject_listbox.place(x=370, y=340, width=310, height=90)

        # Buttons
        Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", command=self.add).place(x=150, y=420, width=110, height=40)
        Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", command=self.update).place(x=270, y=420, width=110, height=40)
        Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", command=self.delete).place(x=390, y=420, width=110, height=40)
        Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", command=self.clear).place(x=510, y=420, width=110, height=40)

        # Search
        Label(self.root, text="Roll No", font=("goudy old style", 15, 'bold'), bg='white').place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg='lightyellow')
        txt_search_roll.place(x=870, y=60, width=200)
        Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", command=self.search).place(x=1070, y=60, width=120, height=28)

        # Table Frame
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=260)

        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        self.StudentTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact", "department", "semester", "state", "city", "pin", "address"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        for col in self.StudentTable["columns"]:
            self.StudentTable.heading(col, text=col.capitalize())

        self.StudentTable["show"] = "headings"
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)


        self.show()

    # def fetch_subjects(self):
    #     try:
    #         dept = self.var_department.get()
    #         sem = self.var_semester.get()
    #         if dept == "Select" or sem == "Select":
    #             messagebox.showerror("Error", "Please select both Department and Semester", parent=self.root)
    #             return

    #         con = sqlite3.connect("rms.db")
    #         cur = con.cursor()
    #         cur.execute("SELECT name FROM subject WHERE department=? AND semester=?", (dept, sem))
    #         rows = cur.fetchall()
    #         self.subject_listbox.delete(0, END)
    #         if rows:
    #             for row in rows:
    #                 self.subject_listbox.insert(END, row[0])
    #         else:
    #             messagebox.showinfo("No Subjects", "No subjects found for selected Department & Semester", parent=self.root)
    #         con.close()
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Failed to fetch subjects due to: {str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Roll No already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO student (roll, name, email, gender, dob, contact, department, semester, state, city, pin, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (self.var_roll.get(), self.var_name.get(), self.var_email.get(), self.var_gender.get(),
                                 self.var_dob.get(), self.var_contact.get(), self.var_department.get(),
                                 self.var_semester.get(), self.var_state.get(), self.var_city.get(),
                                 self.var_pin.get(), self.txt_address.get("1.0", END).strip()))
                    con.commit()
                    messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

                    # # Fetch subjects selected by the student
                    # selected_subjects = [self.subject_listbox.get(i) for i in self.subject_listbox.curselection()]

                    # # Store subjects in student_subject junction table
                    # for subject in selected_subjects:
                    #     cur.execute("INSERT INTO student_subject (student_roll, subject_name) VALUES (?, ?)", (self.var_roll.get(), subject))
                    # con.commit()

                    

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
    
    def get_data(self, ev):
      f = self.StudentTable.focus()
      content = self.StudentTable.item(f)
      row = content['values']
      if row:
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_department.set(row[6])
        self.var_semester.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[11])



    def update(self):
      try:
       if self.var_roll.get() == "":
         messagebox.showerror("Error", "Please select a student from the table", parent=self.root)
         return
      
       con = sqlite3.connect("rms.db")
       cur = con.cursor()
       cur.execute("""
            UPDATE student SET name=?, email=?, gender=?, dob=?, contact=?, department=?, semester=?, state=?, city=?, pin=?, address=?
            WHERE roll=?
        """, (
            # self.var_student_id.get(),
            self.var_name.get(),
            self.var_email.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_contact.get(),
            self.var_department.get(),
            self.var_semester.get(),
            self.var_state.get(),
            self.var_city.get(),
            self.var_pin.get(),
            self.txt_address.get("1.0" ,END).strip(),
            self.var_roll.get()
        ))
       con.commit()
       con.close()
       messagebox.showinfo("Success", "Student record updated successfully", parent=self.root)
       self.show()
       self.clear()
      except Exception as ex:
        messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)


    def delete(self):
      try:
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Please select a student to delete", parent=self.root)
            return
    
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Student record deleted successfully", parent=self.root)
        self.show()
        self.clear()
      except Exception as ex:
        messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_department.set("Select Department")
        self.var_semester.set("Select Semester")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.var_address.set("")
        self.var_a_date.set("")
        self.txt_address.delete("1.0", END)
        self.var_search.set("")

    def search(self):
     try: 
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        query = "SELECT * FROM student WHERE name LIKE ? OR roll LIKE ? OR contact LIKE ?"
        keyword = '%' + self.var_search.get() + '%'
        cur.execute(query, (keyword, keyword, keyword))
        rows = cur.fetchall()
        self.StudentTable.delete(*self.StudentTable.get_children())
        for row in rows:
            self.StudentTable.insert('', END, values=row)
        con.close()
     except Exception as ex:
        messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    
if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
