import numpy
from . import Course, Student


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

    def calculate_average_gpa(self, student: Student):
        __credit = numpy.array([3, 4])
        __marks = numpy.array(list(student.getmark().values()))
        __gpa = numpy.average(__marks, weights=__credit)
        student.setgpa(__gpa)
        return __gpa
