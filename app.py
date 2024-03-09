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
    conn_cursor.execute("SELECT id, name, position, experience, salary, country FROM employees")
    employees_data = conn_cursor.fetchall()
    conn.close()

    return render_template("index.html", employees=employees_data)

@app.route("/selected_employees", methods=["POST"])
def selected_employees():
    search_name = request.form.get("name")
    search_country = request.form.get("country")

    conn = get_db()
    conn_cursor = conn.cursor()

    if search_name:
        conn_cursor.execute("SELECT id, name, position, experience, salary, country FROM employees WHERE name LIKE ?", ('%' + search_name + '%',))
        print("Selected employee name:", search_name)
    elif search_country:
        conn_cursor.execute("SELECT id, name, position, experience, salary, country FROM employees WHERE country LIKE ?", ('%' + search_country + '%',))
        print("Selected country name:", search_country)
    else:
        selected_employees_data = []
        conn.close()
        return render_template("selected_employees.html", selected_employees = selected_employees_data)
    selected_employees_data = conn_cursor.fetchall()
    conn.close()

    return render_template("selected_employees.html", selected_employees=selected_employees_data)

if __name__ == "__main__":
    app.run(debug=True)
