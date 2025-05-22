from app.dbConnect import dbConnect
from app.functions import create_employee, read_employees, update_employee_salary, delete_employee

if __name__ == "__main__":
    conn = dbConnect()
    if conn:
        # USAGE...
        # create_employee(conn, 'Alice', 'Manager', 55000)
        # read_employees(conn)
        # update_employee_salary(conn, 1, 60000)
        # delete_employee(conn, 1)
        conn.close()
        print("Connection closed.")


