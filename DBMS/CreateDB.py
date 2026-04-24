import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subject (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_code TEXT,
        name TEXT,
        department TEXT,
        credits INTEGER,
        professor TEXT,
        semester TEXT,
        duration TEXT
    )
""")


    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        roll TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        department TEXT,
        semester TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student_subject (
        student_roll TEXT,
        subject_id INTEGER,
        FOREIGN KEY (student_roll) REFERENCES student(roll),
        FOREIGN KEY (subject_id) REFERENCES subject(subject_id),
        PRIMARY KEY (student_roll, subject_id)
    )
""")


    cur.execute("""
    CREATE TABLE IF NOT EXISTS result (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT NOT NULL,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        semester TEXT NOT NULL,
        subject TEXT NOT NULL,
        marks_ob INTEGER NOT NULL,
        full_marks INTEGER NOT NULL,
        per REAL NOT NULL,
        FOREIGN KEY (roll) REFERENCES student(roll),
        UNIQUE(roll, subject)
    )
 """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        f_name TEXT,
        l_name TEXT,
        contact TEXT,
        role TEXT,
        email TEXT UNIQUE,
        question TEXT,
        answer TEXT,
        password TEXT
       
    )
    """)

    con.commit()
    con.close()  

create_db()
