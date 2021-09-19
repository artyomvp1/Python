import random
import numpy

print(random.random())    # from 0-1
print(random.uniform(1, 9))    # float
print(random.randint(1, 9))    # 9 included
print(random.randrange(1, 9))    # 9 not included

# Sequences
print(random.choice('Hello'))    # pick random item of a string or a list
print(random.sample([1, 2, 3, 4], 3))    # pick random X UNIQUE items
print(random.choices([1, 2, 3, 4], k=3))    # pick random X NOT UNIQUE items
random.shuffle([1, 2, 3])    # shuffles a list

# Seed - remembers the result of random functions following
random.seed(1)
print(random.random())
random.seed(1)
print(random.random())    # shows the result of the previous random()

