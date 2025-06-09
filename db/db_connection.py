import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Siva@1234",
        database="your_database"  # ⛔ Replace with your actual DB name, e.g., "student_db"
    )
