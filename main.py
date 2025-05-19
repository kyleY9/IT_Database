import mysql.connector


# Functions
def get_connection():
    connection = mysql.connector.connect(user='kyley9',
                                         password='224085274',
                                         host='10.8.37.226',
                                         database='kyley9_db')
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = []
    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()
    return results


def get_student_schedule(student_id):
    query = "CALL Student_Schedule_Procedure(" + str(student_id) + ")"
    return execute_query(get_connection(), query)

def display_student_schedule(student_id):
    for row in get_student_schedule(int(student_id)):
        print("\nPeriod: " + str(row[4]) + "\nCourse: " + row[1] + "\nRoom: " + row[2] + "\nTeacher: " + row[3])

def display_grades

def get_teacher_schedule(teacher_id):
    query = "CALL Teacher_Schedule_Procedure(" + str(teacher_id) + ")"
    return execute_query(get_connection(), query)


def display_teacher_schedule(teacher_id):
    for row in get_teacher_schedule(int(teacher_id)):
        print("\nCourse: " + str(row[1]) + "\nRoom: " + row[2] + "\nPeriod: " + str(row[3]))


# Main Code
choice = input("Are you logging in as a Student or Teacher? ")
if choice.lower() == "student":
    student_id = input("What is your student id? ")
    display_student_schedule(student_id)
elif choice.lower() == "teacher":
    teacher_id = input("What is your teacher id? ")
    display_teacher_schedule(teacher_id)
else:
    print("Sorry, that is not a valid option")
