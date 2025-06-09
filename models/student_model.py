from db.db_connection import get_connection

def add_student(data):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO students 
        (student_id, name, dob, gender, class, section, phone, email, address) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, data)
    conn.commit()
    conn.close()

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    result = cursor.fetchone()
    conn.close()
    return result
