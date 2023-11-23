import numpy as np
import math

x1 = float(input("Enter coordinate X for P1: "))
y1 = float(input("Enter coordinate Y for P1: "))
x2 = float(input("Enter coordinate X for P2: "))
y2 = float(input("Enter coordinate Y for P2: "))

diameter = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
radius = diameter / 2
area = math.pi * radius ** 2
circumference = math.pi * diameter

print("The length of the circle diameter is %0.4f" % (diameter))
print("The circle area and circumference are %0.4f and %0.4f." % (area, circumference))