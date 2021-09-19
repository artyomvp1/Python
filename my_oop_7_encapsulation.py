# Private members - hide when accessing out of the class or scope
# __name
# __method()

# Protected members
# _name
# _method()

# 1
class Edureka():
    def __init__(self):
        self.course = "Python programming course"
        self.__tech = "python"

    def CourseName(self):
        return self.course + self.__tech


ob = Edureka()

# Normal access
print(ob.course)
print(ob.CourseName())

# Access to hidden attr
# print(ob.__tech)    # Provides error because self.tech is private and cannot be called outside the class
print(ob._Edureka__tech)

# 2
class Edureka():
    def __init__(self):
        self.course = "Python programming course"
        self.__tech = "python"

    def CourseName(self):
        return self.course + self.__tech

    def get__tech(self):
        return self.__tech

    def set__tech(self, x):
        self.__tech = x


ob = Edureka()

ob.set__tech('ML')
ob.get__tech()


print(ob.course)
print(ob.CourseName())
print(ob._Edureka__tech)


# 3
class Edureka:
    def __init__(self):
        self.course = 'ML course'
        self.__tech = 'Python'

    def course(self):
        return self.course + ': ' + self.__tech

    def set__tech(self, x):
        self.__tech = x

    def get__tech(self):
        return self.__tech


ob = Edureka()
ob.set__tech('SC learn')
ob.course()
