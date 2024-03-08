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
        self.__marks.setdefault(course_id, "Not enrolled")

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
