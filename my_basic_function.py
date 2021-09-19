# Function and adg
# Parameters - vars that are defined and used in parentheses while defining a function
# Arguments - values passed for these parameters while calling a function

# 1
def print_name(name):       # parameter
    print(name)


print_name('Alex')      # Argument


# Types of arguments
def foo(a, b, c, d=4):      # d - default parameter, can be changed
    print(a, b, c)


foo(1, 2, 3)        # Positional arguments
foo(a=1, b=2, c=3)      # Keyword arguments (order is not important)


# *ARGS **KWARGS
def foo(a, b, *args, **kwargs):    # *args - tuple, **kwargs - dictionary
    print(a, b)
    for i in args:
        print(i)
    for k in kwargs:
        print(k, kwargs[k])


foo(1, 2, 3, 4, 5, six=6, seven=7)    # 1,2 - positional args, 3,4,5 - tuple, 6,7 - kwargs


# Forced keyword arguments
def foo(a, b, *, c, d):
    print(a, b, c, d)


foo(1, 2, c=3, d=4)    # Every parameter after '*' has to be declared as a KEYWORD ARGUMENTS


def foo(*args, c, d):
    print(c, d)


foo(c=5, d=8)    # After *args arguments also have to be declared as KEYWORD ARGUMENTS


# Unpacking arguments
def foo(a, b, c):
    print(a, b, c)


my_list = [0, 2, 3]
foo(*my_list)    # Unpacking parameters to arguments. Length must match number of parameters of a function

my_dict = {'a': 1, 'b': 5, 'c': 9}
foo(**my_dict)    # Unpacking as dict. Dict keys must match the function parameter names


# Local, global variable
#
