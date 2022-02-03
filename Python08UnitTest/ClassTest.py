class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(self):
        self.__num += 1

    @classmethod
    def getNum(self):
        return self.__num

    def __new__(self):
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)


class Student(ClassTest):
    def __init__(self):
        self.name = ''


a = Student()
b = Student()
ClassTest.getNum()
