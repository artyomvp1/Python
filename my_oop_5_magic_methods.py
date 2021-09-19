# Magic (dunder = __) methods change built-in behavior and operations
# init, repr, str - the most common used
# repr, str - what output should look like

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):    # unambiguous representation of an object (for debugging, logging). Put always
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):    # combined pay of two employees
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())    # fullname - method


# Create instances
emp_1 = Employee('Arty', 'Park', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Printing __repr__ without __str__
print(emp_1)

# Printing __repr___ with __str__
print(emp_1)

# Call specifically repr and str
print(repr(emp_1))    # emp_1.__repr__
print(str(emp_1))     # emp_1.__str__

# __add__
print(int.__add__(1, 2))    # general example
print(emp_1 + emp_2)        # without __add__ that wouldn't work

# __len__
print('test'.__len__())    # general example
print(len(emp_1))          # without __len__ that wouldn't work
