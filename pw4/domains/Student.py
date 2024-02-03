class Student:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__marks = {}

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