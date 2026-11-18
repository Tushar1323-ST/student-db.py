import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
        
      )
""")

connection.close()

print("Database and students table created successfully!")