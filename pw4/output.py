from domains import *


def list_courses(school: School):
    print("Courses:")
    for course in school.getcourses():
        print(f"ID: {course.getid()}, Name: {course.getname()}")


def list_students(school: School):
    print("Students:")
    for student in school.getstudents():
        print(
            f"ID: {student.getid()}, Name: {student.getname()}, DoB: {student.getdob()}")


def show_student_marks(school: School):
    if not school.getcourses() or not school.getstudents():
        return
    __selected_course = input("Select a course ID: ")
    print(f"Marks for course {__selected_course}:")
    for student in school.getstudents():
        print(
            f"Student {student.getid()}: {student.getmark().get(__selected_course, 'Not enrolled')}")


def show_student_gpas(school: School):
    if not school.getcourses() or not school.getstudents():
        return

    for student in school.getstudents():
        print(
            f"Student {student.getid()}: {school.calculate_average_gpa(student)}")

    gpas = {student.getid(): school.calculate_average_gpa(student)
            for student in school.getstudents()}
    sorted_gpas = sorted(gpas.items(), key=lambda x: x[1], reverse=True)
    print("\nGPA from highest to lowest:")
    for student_id, gpa in sorted_gpas:
        print(f"Student {student_id}: {gpa}")
