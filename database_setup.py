import sqlite3
import random
import numpy as np
from datetime import datetime
from faker import Faker

fake = Faker()

DATABASE = "employees.db"

def generate_random_salary():
    salary = round(np.random.normal(65000, 15000), 2)
    formatted_salary = "${:,.0f}".format(salary)
    return formatted_salary

def generate_random_experience():
    experience = fake.date_time_between(start_date="-20y", end_date="now").date()
    exp_years = datetime.now().year - experience.year
    return f"{exp_years} years"

def generate_random_position():
    return fake.job()

def generate_random_name():
    return fake.name()

def generate_random_country():
    return fake.country()


def create_and_populate_database():
    conn = sqlite3.connect(DATABASE)
    conn_cursor = conn.cursor()

    conn_cursor.execute('''CREATE TABLE IF NOT EXISTS
                        employees (id INTEGER PRIMARY KEY,
                        name TEXT,
                        position TEXT,
                        experience DATE,
                        salary TEXT,
                        country TEXT)
                    ''')

    for _ in range(30000):
        name = generate_random_name()
        position = generate_random_position()
        experience = generate_random_experience()
        salary = generate_random_salary()
        country = generate_random_country()

        conn_cursor.execute('''INSERT INTO employees
                     (name, position, experience, salary, country)
                     VALUES(?, ?, ?, ?, ?)''', (name, position, experience, salary, country))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_database()
