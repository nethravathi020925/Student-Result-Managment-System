import sqlite3

con = sqlite3.connect("rms.db")
cur = con.cursor()
cur.execute("SELECT * FROM subject")
rows = cur.fetchall()
for row in rows:
    print(row)
