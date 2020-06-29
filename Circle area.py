#Circle area
from math import pi

d = float(input('Diameter: '))
r = d/2
a = pi*r**2
c = 2*pi*r
print(f'''The circle area is: {a:.2f}
The circle circunference is: {c:.2f}''')