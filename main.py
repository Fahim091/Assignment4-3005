import psycopg2

# database connection details
db_params = {
    'host': 'localhost',
    'database': 'Assignment4',
    'user': 'postgres',
    'password': 'Namak123'
}

def getAllStudents():
    # Execute a SELECT query to retrieve all students
    cursor.execute("SELECT * FROM students")
    # Fetch all rows
    rows = cursor.fetchall()
    # Print the result
    for row in rows:
        print(row)

def addStudent(first_name, last_name, email, enrollment_date):
    # Check if the email already exists
    cursor.execute("SELECT COUNT(*) FROM students WHERE email = %s", (email,))
    email_exists = cursor.fetchone()[0] > 0

    if not email_exists:
        # Email doesn't exist, proceed with the insertion
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, email, enrollment_date)

        cursor.execute(query, values)
        # Commit the query
        connection.commit()
        print("Student added successfully!")

    else:
        print(f"Student with email {email} already exists!")

def updateStudentEmail(student_id, new_email):
    # Check if the new email already exists
    cursor.execute("SELECT COUNT(*) FROM students WHERE email = %s AND student_id != %s", (new_email, student_id))
    email_exists = cursor.fetchone()[0] > 0

    if not email_exists:
        # Email doesn't exist, proceed with the update
        query = "UPDATE students SET email = %s WHERE student_id = %s"
        values = (new_email, student_id)

        cursor.execute(query, values)
        # Commit the query
        connection.commit()
        print(f"Email for student_id {student_id} updated successfully!")

    else:
        print(f"Email {new_email} already exists for another student!")

def deleteStudent(student_id):
    # Check if the student with the specified ID exists
    cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = %s", (student_id,))
    student_exists = cursor.fetchone()[0] > 0

    if student_exists:
        # Student exists, proceed with the deletion
        query = "DELETE FROM students WHERE student_id = %s"
        values = (student_id,)

        cursor.execute(query, values)
        # Commit the query
        connection.commit()
        print(f"Student with student_id {student_id} deleted successfully!")

    else:
        print(f"Student with student_id {student_id} does not exist!")


# Establish a connection to the database
try:
    connection = psycopg2.connect(**db_params)
    print("Connected to the database!")

    # Create a cursor object to interact with the database
    with connection.cursor() as cursor:
        # Example: Select all students
        # getAllStudents()
        
        # #Example: Add a student
        # addStudent('Fahim2', 'Ali', 'FahimAli2@gmail.com', '2023-01-01')
        # getAllStudents()
        
        # #Example: Update a student's email
        # updateStudentEmail(1, 'FahimAli3@gmail.com')
        # getAllStudents()
        
        #Example: Delete a student
        deleteStudent(16)
        getAllStudents()
        
except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the database connection outside the try-except block
    if connection:
        connection.close()
        print("Connection closed.")
