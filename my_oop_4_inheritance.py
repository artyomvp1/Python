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


class Developer(Employee):

    raise_amount = 1.09    # Override the parent class variable

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)    # Inherit attributes of the parent class.
        # Employee.__init__(self, first, last, pay)    # 2nd way to inherit
        self.language = language


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):    # Default value
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for i in self.employees:
            print("-->", i.fullname())


# Create instances of subclass developer
dev_1 = Developer('Arty', 'Park', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

# Calling attributes of a subclass
print(dev_1.email)

# Create instance of subclass manager
mgr_1 = Manager('Sam', 'Smith', 95000, [dev_1])
print(mgr_1.email)

# Check manager's employee list before and after
mgr_1.print_emps()    # list before adding
mgr_1.add_emp(dev_2)    # add a new employee
mgr_1.print_emps()    # list after adding

# isinstance() - shows if an instance is an object of a class
print(isinstance(mgr_1, Employee))    # Employee - parent class for manager

# issubclass() - shows if a class is a subclass of another class
print(issubclass(Developer, Employee))
