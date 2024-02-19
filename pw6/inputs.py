from domains import *
import pathlib as path


def input_student_info(school):
    __num_students = int(input("Enter the number of students: "))
    filename = './data/students.txt'

    for _ in range(__num_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        school.add_student(Student.Student(id, name, dob))
        studentinfo = f"{id}\n{name}\n{dob}\n"

        try:
            with open(filename, 'a+') as f:
                f.write(studentinfo)
        except IOError:
            print(f"Something happened with {filename}")


def input_course_info(school):
    __num_courses = int(input("Enter the number of courses: "))
    filename = "./data/courses.txt"
    for _ in range(__num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        school.add_course(Course.Course(id, name))
        courseinfo = f"{id}\n{name}\n"

        try:
            with open(filename, 'a+') as f:
                f.write(courseinfo)
        except IOError:
            print(f"Something happened with {filename}")


def input_student_marks(school):
    filename = "./data/marks.txt"

    if not school.getcourses():
        print("There are no courses in the database!")
        return
    __selected_course = input("Select a course ID: ")

    for student in school.getstudents():
        try:
            marks = round(
                float(input(f"Enter marks for student {student.getid()} in course {__selected_course}: ")), 1)
            student.add_mark(__selected_course, marks)
            pass
        except ValueError:
            print("Float or else....\n")
            continue

        studentmark = f"{student.getid()}\n{marks}\n{__selected_course}\n"

        try:
            with open(filename, 'a+') as f:
                f.write(studentmark)
        except IOError:
            print(f"Something happened with {filename}")
