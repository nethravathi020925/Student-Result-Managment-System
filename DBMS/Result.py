from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("College Student Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===title===
        title = Label(self.root, text="Add Student Results", font=("goudy old style", 20, "bold"),
                      bg="#4B0082", fg="white")
        title.pack(side=TOP, fill=X)

        # =========variables=====
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_semester = StringVar()
        self.var_subject = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.subject_list = []
        self.selected_subjects = []  # Store added results before saving

        # =========widgets=====
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_select.place(x=50, y=100)

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_name.place(x=50, y=160)

        lbl_department = Label(self.root, text="Department", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_department.place(x=50, y=220)

        lbl_semester = Label(self.root, text="Semester", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_semester.place(x=50, y=280)

        lbl_subject = Label(self.root, text="Subject", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_subject.place(x=50, y=340)

        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_marks.place(x=50, y=400)

        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_full_marks.place(x=50, y=460)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list,
                                        font=("goudy old style", 15, "bold"), cursor="hand2", state="readonly")
        self.txt_student.place(x=280, y=100, width=200)
        self.fetch_roll()

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"),
                            bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=500, y=100, width=120, height=28)

        txt_name_roll = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, 'bold'),
                              bg='lightyellow', state='readonly')
        txt_name_roll.place(x=280, y=160, width=300)

        txt_department_roll = Entry(self.root, textvariable=self.var_department, font=("goudy old style", 20, 'bold'),
                                    bg='lightyellow', state='readonly')
        txt_department_roll.place(x=280, y=220, width=300)

        txt_semester_roll = Entry(self.root, textvariable=self.var_semester, font=("goudy old style", 20, 'bold'),
                                  bg='lightyellow', state='readonly')
        txt_semester_roll.place(x=280, y=280, width=300)

        self.subject_combo = ttk.Combobox(self.root, textvariable=self.var_subject, values=self.subject_list,
                                          font=("goudy old style", 15, 'bold'), state="readonly", cursor="hand2")
        self.subject_combo.place(x=280, y=340, width=300)

        txt_marks_roll = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, 'bold'),
                               bg='lightyellow')
        txt_marks_roll.place(x=280, y=400, width=300)

        txt_full_marks_roll = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, 'bold'),
                                    bg='lightyellow')
        txt_full_marks_roll.place(x=280, y=460, width=300)

        # ========buttons====
        btn_add = Button(self.root, text='Submit', font=("times new roman", 15, "bold"),
                         bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.add_result)
        btn_add.place(x=300, y=520, width=120, height=35)

        btn_update = Button(self.root, text='Update', font=("times new roman", 15, "bold"),
                            bg="lightblue", activebackground="lightblue", cursor="hand2", command=self.update_subject)
        btn_update.place(x=439, y=520, width=120, height=35)

        btn_delete = Button(self.root, text='Delete', font=("times new roman", 15, "bold"),
                            bg="red", fg="white", activebackground="red", cursor="hand2", command=self.delete_subject)
        btn_delete.place(x=560, y=520, width=120, height=35)

        btn_clear = Button(self.root, text='Clear', font=("times new roman", 15, "bold"),
                           bg="lightgray", activebackground="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=690, y=520, width=120, height=35)

       


        #----------------- image ------------------
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((800, 400), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=700, y=100, width=800, height=400)
        self.lbl_bg.lower()  # Make sure image is behind other widgets


        # btn_save_all = Button(self.root, text='Save All', font=("times new roman", 15, "bold"),
        #                       bg="orange", activebackground="orange", cursor="hand2", command=self.submit_results)
        # btn_save_all.place(x=560, y=520, width=120, height=35)

    def fetch_roll(self):
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            self.roll_list = [row[0] for row in rows]
            self.txt_student['values'] = self.roll_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching roll numbers: {str(ex)}")

    def fetch_subjects(self):
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            dept = self.var_department.get()
            sem = self.var_semester.get()
            cur.execute("SELECT name FROM subject WHERE department=? AND semester=?", (dept, sem))
            rows = cur.fetchall()
            self.subject_list = [row[0] for row in rows]
            self.subject_combo['values'] = self.subject_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching subjects: {str(ex)}")

    def search(self):
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("SELECT name, department, semester FROM student WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_department.set(row[1])
                self.var_semester.set(row[2])
                self.fetch_subjects()
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Search failed: {str(ex)}")



    def add_result(self):
       try:
        subject = self.var_subject.get()
        marks = self.var_marks.get()
        full_marks = self.var_full_marks.get()

        if not subject or not marks or not full_marks:
            messagebox.showerror("Error", "Please fill all fields", parent=self.root)
            return

        if not marks.isdigit() or not full_marks.isdigit():
            messagebox.showerror("Error", "Marks must be numeric", parent=self.root)
            return

        if int(full_marks) == 0:
            messagebox.showerror("Error", "Full Marks cannot be zero", parent=self.root)
            return

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        # Check for existing result
        cur.execute("SELECT * FROM result WHERE roll=? AND subject=?", (self.var_roll.get(), subject))
        if cur.fetchone():
            messagebox.showerror("Error", f"Result for subject '{subject}' already exists.", parent=self.root)
            return

        # Calculate percentage
        per = (int(marks) * 100) / int(full_marks)

        # Insert into database
        cur.execute("""INSERT INTO result 
            (roll, name, department, semester, subject, marks_ob, full_marks, per) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (self.var_roll.get(), self.var_name.get(), self.var_department.get(), self.var_semester.get(),
             subject, marks, full_marks, f"{per:.2f}")
        )
        con.commit()
        con.close()

        messagebox.showinfo("Success", f"Result for '{subject}' saved successfully.", parent=self.root)

        # Clear subject fields only (not student)
        self.var_subject.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
        self.subject_combo.set("")

       except Exception as ex:
        messagebox.showerror("Error", f"Error adding result: {str(ex)}", parent=self.root)

    def update_subject(self):
        try:
          subject = self.var_subject.get()
          marks = self.var_marks.get()
          full_marks = self.var_full_marks.get()

          if not subject or not marks or not full_marks:
            messagebox.showerror("Error", "Please fill all fields", parent=self.root)
            return

          if not marks.isdigit() or not full_marks.isdigit():
            messagebox.showerror("Error", "Marks must be numeric", parent=self.root)
            return

          if int(full_marks) == 0:
            messagebox.showerror("Error", "Full Marks cannot be zero", parent=self.root)
            return

          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()

            # Check if result exists
          cur.execute("SELECT * FROM result WHERE roll=? AND subject=?", (self.var_roll.get(), subject))
          if not cur.fetchone():
            messagebox.showerror("Error", f"No existing result for subject '{subject}' to update.", parent=self.root)
            return

            # Calculate percentage
          per = (int(marks) * 100) / int(full_marks)

            # Update the result
          cur.execute("""
                UPDATE result SET
                    marks_ob=?, full_marks=?, per=?
                WHERE roll=? AND subject=?
            """, (marks, full_marks, f"{per:.2f}", self.var_roll.get(), subject))
          con.commit()
          con.close()

          messagebox.showinfo("Success", f"Result for '{subject}' updated successfully.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error updating result: {str(ex)}", parent=self.root)

    def delete_subject(self):
        try:
            subject = self.var_subject.get()

            if not subject:
                messagebox.showerror("Error", "Please select subject to delete", parent=self.root)
                return

            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()

            # Check if result exists
            cur.execute("SELECT * FROM result WHERE roll=? AND subject=?", (self.var_roll.get(), subject))
            if not cur.fetchone():
                messagebox.showerror("Error", f"No result found for subject '{subject}' to delete.", parent=self.root)
                return

            # Confirm before deleting
            ask = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete result for '{subject}'?", parent=self.root)
            if ask:
                cur.execute("DELETE FROM result WHERE roll=? AND subject=?", (self.var_roll.get(), subject))
                con.commit()
                con.close()

                messagebox.showinfo("Success", f"Result for '{subject}' deleted successfully.", parent=self.root)

                # Clear subject and marks fields
                self.var_subject.set("")
                self.var_marks.set("")
                self.var_full_marks.set("")
                self.subject_combo.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error deleting result: {str(ex)}", parent=self.root)


    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_semester.set("")
        self.var_subject.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
        self.selected_subjects.clear()
        self.subject_combo.set("")


if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
