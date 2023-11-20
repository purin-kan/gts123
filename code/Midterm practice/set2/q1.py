import math

surface_area = 0

shape = input("Input a shape T/S/C: ")
length = input("Input a length: ")

if not shape in ['T', 'S', 'C']:
    print("Type must be only T/S/C.")
    exit()
    
if not length.isdigit() or int(length) < 0:
    print("Length must be more than or equal to zero.")
    exit()


length = int(length)

if shape == 'T':
    shape = "triangle"
    surface_area = length * length / 4
elif shape == 'S':
    shape = "square"
    surface_area = length * length / 2
elif shape == 'C':
    shape = "circle"
    surface_area = math.pi * ((length / 2) ** 2)


print("The surface area of %s is %.2f" % (shape, surface_area))
