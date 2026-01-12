# DAL --- DATA ACCESS LAYER

from database.connection import get_connection

def insert_employees(id, name, role, department_id, salary):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Employees (id, name, role, department_id, salary) VALUES(%s, %s, %s, %s, %s)", 
        (id, name, role, department_id, salary)
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Employees")

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_employee_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Employees WHERE id = %s", (id, )
    )

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def get_employee_by_name(name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Employees WHERE name = %s", 
        (name, )
    )

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_employee_by_role(role):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Employees WHERE role = %s", 
        (role,)
    )

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_employee_by_department_id(department_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Employees WHERE department_id = %s", 
        (department_id,)
    )
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_employee_by_salary(salary):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Employees WHERE salary = %s", 
        (salary, )
    )

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def update_name(id, name):
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "UPDATE Employees SET name = %s WHERE id = %s",
        (name, id)
    )

    conn.commit()
    cursor.close()
    conn.close()

def update_role(id, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Employees SET role = %s WHERE id = %s",
        (role, id)
    )

    conn.commit()
    cursor.close()
    conn.close()

def update_department_id(id, department_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Employees SET department_id = %s WHERE id = %s",
        (department_id, id)
    )

    conn.commit()
    cursor.close()
    conn.close()

def update_salary(id, salary):
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "UPDATE Employees SET salary = %s WHERE id = %s", 
        (salary, id)
    )
    conn.commit()
    cursor.close()
    conn.close()
  
