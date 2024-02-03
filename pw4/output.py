from domains import *


def list_courses():
    print("Courses:")
    for course in School.__courses:
        print(f"ID: {course.getid()}, Name: {course.getname()}")


def list_students():
    print("Students:")
    for student in School.__students:
        print(
            f"ID: {student.getid()}, Name: {student.getname()}, DoB: {student.getdob()}")


def show_student_marks():
    if not School.__courses or not School.__students:
        return
    __selected_course = input("Select a course ID: ")
    print(f"Marks for course {__selected_course}:")
    for student in School.__students:
        print(
            f"Student {student.getid()}: {student.getmark().get(__selected_course, 'Not enrolled')}")


def show_student_gpas():
    if not School.__courses or not School.__students:
        return
    __selected_course = input("Select a course ID: ")
    print(f"Marks for course {__selected_course}:")
    for student in School.__students:
        print(f"Student {student.getid()}: {School.calculate_average_gpa}")
