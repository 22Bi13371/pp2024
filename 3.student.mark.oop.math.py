import math
import numpy
import curses


class Student:
    __gpa = 0

    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def setgpa(self, gpa):
        self.__gpa = gpa

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name

    def getdob(self):
        return self.__dob

    def getmark(self):
        return self.__marks

    def getgpa(self):
        return self.__gpa


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name


class School:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def input_student_info(self):
        __num_students = int(input("Enter the number of students: "))
        for _ in range(__num_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.add_student(Student(id, name, dob))

    def input_course_info(self):
        __num_courses = int(input("Enter the number of courses: "))
        for _ in range(__num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.add_course(Course(id, name))

    def input_student_marks(self):
        if not self.__courses:
            print("There are no courses in the database!")
            return
        __selected_course = input("Select a course ID: ")
        for student in self.__students:
            try:
                marks = round(
                    float(input(f"Enter marks for student {student.getid()} in course {__selected_course}: ")), 1)
                student.add_mark(__selected_course, marks)
                pass
            except ValueError:
                print("Float or else....\n")
                continue

    def calculate_average_gpa(student):
        __credit = numpy.array([3, 4])
        __marks = numpy.array(list(student.getmark().values()))
        __gpa = numpy.average(__marks, weights=__credit)
        student.setgpa(__gpa)
        return __gpa

    def list_courses(self):
        print("Courses:")
        for course in self.__courses:
            print(f"ID: {course.getid()}, Name: {course.getname()}")

    def list_students(self):
        print("Students:")
        for student in self.__students:
            print(
                f"ID: {student.getid()}, Name: {student.getname()}, DoB: {student.getdob()}")

    def show_student_marks(self):
        if not self.__courses or not self.__students:
            return
        __selected_course = input("Select a course ID: ")
        print(f"Marks for course {__selected_course}:")
        for student in self.__students:
            print(
                f"Student {student.getid()}: {student.getmark().get(__selected_course, 'Not enrolled')}")

    def show_student_gpas(self):
        if not self.__courses or not self.__students:
            return

        for student in self.__students:
            print(
                f"Student {student.getid()}: {School.calculate_average_gpa(student)}")

        gpas = {student.getid(): School.calculate_average_gpa(student)
                for student in self.__students}
        sorted_gpas = sorted(gpas.items(), key=lambda x: x[1], reverse=True)
        print("\nGPA from highest to lowest:")
        for student_id, gpa in sorted_gpas:
            print(f"Student {student_id}: {gpa}")


def main():
    school = School()
    while True:
        print_menu = "-----------MENU----------- \n0)Exit program \n1)Input student(s) info \n2)Input course(s) info \n3)Input student marks \n4)List courses \n5)List students \n6)List student marks \n7)List student GPAs"
        print(print_menu)
        try:
            menu_selector = int(input("You chose? "))
            pass
        except ValueError:
            print("Integer or else....\n")
            continue

        match menu_selector:
            case 0:
                print("Exitting program...")
                break
            case 1:
                school.input_student_info()
            case 2:
                school.input_course_info()
            case 3:
                school.input_student_marks()
            case 4:
                school.list_courses()
            case 5:
                school.list_students()
            case 6:
                school.show_student_marks()
            case 7:
                school.show_student_gpas()
            case _:
                print("Invalid option!")
                continue


if __name__ == "__main__":
    main()
