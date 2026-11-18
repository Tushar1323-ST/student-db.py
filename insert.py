import sqlite3

Connection = sqlite3.connect("students.db")

Connection.execute(
"INSERT INTO students (name, age, course) VALUES (?,?,?)",
                      ("Rahul",20,"python"))

Connection.commit()
Connection.close()


print("Record inserted successfully!")