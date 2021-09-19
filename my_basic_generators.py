# Generators - functions that return objects that can be iterated
# Functions with "yield" keyword instead of "return" keyword
# Faster
# NEXT function - one of a time
def my_gen(x):
    while x > 0:
        yield x
        x -= 1


result = my_gen(10)
print(next(result))

for i in range(9):
    print(next(result))
print()


# Fibonacci sequence
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


result = fibonacci(30)
for i in result:
    print(i)
print()


# Generator expressions (same way list comprehension)
gen_expr = (i for i in range(10) if i % 2 == 0)    # () instead of []
for i in gen_expr:
    print(i)


# Class generator
class Iter:
    def __init__(self, maxvalue, increment):
        self.maxvalue = maxvalue
        self.increment = increment
        self.currentvalue = 0

    def __next__(self):
        if self.currentvalue < self.maxvalue:
            self.currentvalue += self.increment
            return self.currentvalue
        else:
            raise StopIteration


if __name__ == "__main__":
    xx = Iter(10, 1)

    for i in range(11):
        print(next(xx))