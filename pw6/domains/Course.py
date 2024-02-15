class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name
