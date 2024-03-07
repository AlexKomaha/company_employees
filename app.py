from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = "employees.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    conn = get_db()
    conn_cursor = conn.cursor()
    conn_cursor.execute("SELECT id, name, position, hire_date, salary, city, country FROM employees")
    employees_data = conn_cursor.fetchall()
    conn.close()
    
    return render_template("index.html", employees=employees_data)

@app.route("/selected_employees", methods=["POST"])
def selected_employees():
    selected_employee_names = request.form.getlist("name")
    print("Selected employee names:", selected_employee_names)
    
    conn = get_db()
    conn_cursor = conn.cursor()

    selected_employees_data = []
    for employee_name in selected_employee_names:
        conn_cursor.execute("SELECT id, name, position, hire_date, salary, city, country FROM employees WHERE name = ?", (employee_name,))
        selected_employee_data = conn_cursor.fetchone()
        selected_employees_data.append(selected_employee_data)
    conn.close()
    
    return render_template("selected_employees.html", selected_employees=selected_employees_data)

if __name__ == "__main__":
    app.run(debug=True)
