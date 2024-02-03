from domains import *


def list_courses(school):
    print("Courses:")
    for course in school.getcourses():
        print(f"ID: {course.getid()}, Name: {course.getname()}")


def list_students(school):
    print("Students:")
    for student in school.getstudents():
        print(
            f"ID: {student.getid()}, Name: {student.getname()}, DoB: {student.getdob()}")


def show_student_marks(school):
    if not school.getcourses() or not school.getstudents():
        return
    __selected_course = input("Select a course ID: ")
    print(f"Marks for course {__selected_course}:")
    for student in school.getstudents():
        print(
            f"Student {student.getid()}: {student.getmark().get(__selected_course, 'Not enrolled')}")


def show_student_gpas(school):
    if not school.getcourses() or not school.getstudents():
        return
    __selected_course = input("Select a course ID: ")
    print(f"Marks for course {__selected_course}:")
    for student in school.getstudents():
        print(f"Student {student.getid()}: {school.calculate_average_gpa}")
