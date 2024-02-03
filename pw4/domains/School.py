import numpy
from domains import Course, Student


class School:
    __students = []
    __courses = []

    def __init__(self):
        self.__students = []
        self.__courses = []

    def getstudents(self):
        return self.__students

    def getcourses(self):
        return self.__courses

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def calculate_average_gpa(student):
        marks = numpy.array(list(student.getmark(student).values()))
        gpa = numpy.mean(marks)
        return gpa
