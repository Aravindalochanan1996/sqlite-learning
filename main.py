import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute(
    "INSERT INTO employee(name, age) VALUES(?, ?)",
    ("Aravind", 29)
)

conn.commit()

cursor.execute("SELECT * FROM employee")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()