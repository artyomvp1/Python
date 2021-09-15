# @property provides using a method as an attribute, to not change the whole code

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'    # @property allows using email method as an attribute

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, var):
        first, last = var.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# emp_1.first = 'Jim'     # Problem: Changed attr but fullname method shows the old first name

emp_1.fullname = 'Artem Park'    # setter parsed the name, and applied to all attr and methods

print(emp_1.first)
print(emp_1.email)    # email is method we are accessing it like an attribute
print(emp_1.fullname)

del emp_1.fullname    # delete via deleter
