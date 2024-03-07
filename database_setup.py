import sqlite3
import random
import numpy as np
from faker import Faker

fake = Faker()

DATABASE = "employees.db"

def generate_random_salary():
    return round(np.random.normal(65000, 15000),2)

def generate_random_hire_date():
    return fake.date_time_between(start_date="-5y", end_date="now").date()

def generate_random_position():
    return fake.job()

def generate_random_name():
    return fake.name()

def generate_random_city():
    return fake.city()

def generate_random_country():
    return fake.country()


def create_and_populate_database():
    conn = sqlite3.connect(DATABASE)
    conn_cursor = conn.cursor()
    
    conn_cursor.execute('''CREATE TABLE IF NOT EXISTS
                        employees (id INTEGER PRIMARY KEY,
                        name TEXT,
                        position TEXT,
                        hire_date DATE,
                        salary INTEGER,
                        city TEXT,
                        country TEXT)
                    ''')
    
    for _ in range(30): 
        name = generate_random_name()
        position = generate_random_position()
        hire_date = generate_random_hire_date()
        salary = generate_random_salary()
        city = generate_random_city()
        country = generate_random_country()

        conn_cursor.execute('''INSERT INTO employees
                     (name, position, hire_date, salary, city, country) 
                     VALUES(?, ?, ?, ?, ?, ?)''', (name, position, hire_date, salary, city, country))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_database()



