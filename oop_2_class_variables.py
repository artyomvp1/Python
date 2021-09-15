# Class variables - parameter that is the same for each instance

class Employee:

    raise_amount = 1.04  # class variable (attribute)
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1  # Whenever new instance is created (init) count +1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):  # method to apply pay raise
        self.pay = int(self.pay * self.raise_amount)


# Create instances
emp_1 = Employee('Arty', 'Park', 50000)
emp_2 = Employee('Test', 'User', 50000)
print(f"Original raise for both instances:\t{emp_1.raise_amount} {emp_2.raise_amount}")

# Changing a class variable
Employee.raise_amount = 1.05
print(f"After changing a class variable:\t{emp_1.raise_amount} {emp_2.raise_amount}")

# Changing a class variable for a certain instance
emp_2.raise_amount = 1.06
print(f"After changing for 2nd instance:\t{emp_1.raise_amount} {emp_2.raise_amount}")

# Counting number of employees
print(f"Number of employees:\t\t\t\t{Employee.num_of_employees}")
