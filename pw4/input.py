from domains import *


def input_student_info():
    __num_students = int(input("Enter the number of students: "))
    for _ in range(__num_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        School.add_student(Student(id, name, dob))


def input_course_info():
    __num_courses = int(input("Enter the number of courses: "))
    for _ in range(__num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        School.add_course(Course(id, name))


def input_student_marks():
    if not School.__courses:
        print("There are no courses in the database!")
        return
    __selected_course = input("Select a course ID: ")
    for student in School.__students:
        try:
            marks = round(
                float(input(f"Enter marks for student {student.getid()} in course {__selected_course}: ")), 1)
            student.add_mark(__selected_course, marks)
            pass
        except ValueError:
            print("Float or else....\n")
            continue
