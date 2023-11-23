import math

def myCylinder(r, h):
    return (math.pi * r ** 2 * h, 2 * math.pi * r * (r + h))

r = input("Enter the radius r of the cylinder: ")
h = input("Enter the height h of the cylinder: ")

try:
    r = float(r)
    h = float(h)
except ValueError:
    print("Invalid input")
    exit()

print("The volume is %.2f and the surface area is %.2f" % (myCylinder(r, h)[0], myCylinder(r, h)[1]))
