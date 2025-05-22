from mysql.connector import Error

def create_employee(connection, name, position, salary):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, position, salary))
        connection.commit()
        print("Employee inserted successfully.")
    except Error as err:
        print(f"Failed to insert employee: {err}")

def read_employees(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM employees"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    except Error as err:
        print(f"Failed to read employees: {err}")

def update_employee_salary(connection, employee_id, new_salary):
    try:
        cursor = connection.cursor()
        query = "UPDATE employees SET salary = %s WHERE id = %s"
        cursor.execute(query, (new_salary, employee_id))
        connection.commit()
        print("Employee salary updated successfully.")
    except Error as err:
        print(f"Failed to update salary: {err}")

def delete_employee(connection, employee_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM employees WHERE id = %s"
        cursor.execute(query, (employee_id,))
        connection.commit()
        print("Employee deleted successfully.")
    except Error as err:
        print(f"Failed to delete employee: {err}")
