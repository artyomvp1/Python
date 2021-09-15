# Class - the way to logically group data (attributes) and functions (methods)
# Class - a blue print to create instances
# Instance - ?
# Instance variable - contain data which is unique for each instance
# Init - constructor. A parameter passed automatically and set all self attributes. Called whenever an object is created
# Self - variable represents an instance of the object

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last


# Create instances
emp_1 = Employee('Arty', 'Park', 50000)  # Instance 1
emp_2 = Employee('Test', 'User', 60000)  # Instance 2

# Call instance attribute
print(f"Call instance attribute:\t{emp_1.email}")

# Call a method
print(f"Call a method:\t\t\t\t{emp_1.fullname()}")
