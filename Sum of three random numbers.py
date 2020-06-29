#The sum of three random numbers between 1 and 99
import random

a = random.randint(1, 99)
b = random.randint(1, 99)
c = random.randint(1, 99)

d = a+b+c

print(f'{a} + {b} + {c} = {d}')