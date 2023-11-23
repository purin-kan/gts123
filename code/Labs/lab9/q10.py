import math

def SquareArea(x):
    return x ** 2

def CircleArea(x):
    return math.pi * x ** 2

choice = input("Do you want to find the area of a square (s) or a circle (c)?: ")
if choice not in ['s', 'c']:
    print("Wrong input")
    exit()
length = input("Enter the length: ")

try:
    length = float(length)
except ValueError:
    print("Wrong input")
    exit()

if choice == 's':
    print("The area of the square is %.2f" % SquareArea(length))
elif choice == 'c':
    print("The area of the circle is %.2f" % CircleArea(length))
