# Assignment4-3005
Link to youtube video: https://youtu.be/WTLqo2O_BL4

Database Setup Instructions:
Prerequisites: PostgreSQL

Steps: 
    - Launch pgAdmin4
    - Create a new database 
    - Create the 'students' table
        - CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            enrollment_date DATE
        );


Compiling and running application:
Prerequisites: Python installed and psycopg2 library 

Steps: 
    - Run the application by typing 'python main.py' in the terminal in the right directory or click the run button


Application Functions Explained: 
    - getAllStudents()
        Description: Retrieves all students from the database.
        Usage: getAllStudents()
    - addStudent(first_name, last_name, email, enrollment_date)
        Description: Adds a new student to the database after checking for duplicate emails.
        Parameters:
            first_name: First name of the student.
            last_name: Last name of the student.
            email: Email address of the student.
            enrollment_date: Date of enrollment for the student.
        Usage: addStudent('Fahim', 'Ali', 'FahimAli@example.com', '2023-11-22')
    - updateStudentEmail(student_id, new_email)
        Description: Updates the email address for a student with the specified student_id after checking for duplicate emails.
        Parameters:
            student_id: ID of the student to be updated.
            new_email: New email address for the student.
        Usage: updateStudentEmail(1, 'new.email@example.com')
    - deleteStudent(student_id)
        Description: Deletes the record of the student with the specified student_id from the database after checking the id exists.
        Parameters:
            student_id: ID of the student to be deleted.
        Usage: deleteStudent(1)
