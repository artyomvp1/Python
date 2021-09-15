import datetime
# Regular method - auto take the instance as the first argument (self - by convention)
# Class method - auto take CLASS as the first argument. We are working with a class instead of instance
# Static method - doesn't pass anything, doesn't change a class, but has a logical relation to the class


class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):  # 1 - to manipulate class variables
        cls.raise_amount = amount

    @classmethod  # 2 - use as alternative constructor (different ways to create objects)
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # doesn't change anything in our class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # 0 - Monday, 6 - Sunday
            return False
        else:
            return True


# Create instances
emp_1 = Employee('Arty', 'Park', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Calling a class method to change class variable (working with a class, instead of instance)
Employee.set_raise_amount(1.11)
print(f"After calling a class method:\t{emp_1.raise_amount}")

# Use class method as alternative constructor, parsing a string/list
emp_str_1 = 'John-Doe-75000'  # string/list to parse
emp_3 = Employee.from_string(emp_str_1)  # create new instance using the class method
print(f"New instance via class method:\t{emp_3.first}, {emp_3.last}, {emp_3.pay}")

# Calling a static method
my_date = datetime.date(2016, 7, 10)
print(f"Is a variable a weekday:\t\t{Employee.is_workday(my_date)}")
