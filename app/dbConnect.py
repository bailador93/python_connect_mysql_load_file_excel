import mysql.connector
from mysql.connector import Error
import getpass

def dbConnect():
    try:
        password = getpass.getpass("Enter password to connect to the database: ")
        connection = mysql.connector.connect(
            user='root',
            password=password if password else '',
            host='localhost',
            database='python_load_excel_employee'
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as err:
        print(f"Error connecting to the database: {err}")
        return None
