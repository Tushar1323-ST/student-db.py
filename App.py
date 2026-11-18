from flask import Flask,jsonify,request
import sqlite3

app = Flask(__name__)

def get_database_Connecttion():
    Connection = sqlite3.connect("students.db")
    Connection.row_factory = sqlite3.Row
    return Connection

@app.route("/")
def home():
    return "Welcome to the Home page of student management project"

@app.route("/student")
def students():
    Connection = get_database_Connecttion()

    students = Connection.execute("SELECT * FROM students").fetchall()
    Connection.close()
    students_list = []

    for student in students:
        students_list.append(dict(student))

    return jsonify(students_list)

@app.route("/student", methods=["POST"])
def add_student():
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    course = data["course"]

    Connection = get_database_Connecttion()
    Connection.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    Connection.commit()
    Connection.close()

    return jsonify({"message": "Student record added successfully"})

@app.route("/student/<int:id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    connection = get_database_Connecttion()
    connection.execute("UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?", (data["name"], data["age"], data["course"], student_id))
    connection.commit()
    connection.close()

    return jsonify({"message": "Student record updated successfully"})

@app.route("/student/<int:id>", methods=["DELETE"])
def delete_student(student_id):
    connection = get_database_Connecttion()
    connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "Student record deleted successfully"})

if __name__=="__main__":
    app.run(debug=True)


