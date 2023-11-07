import math

def CirArea(r):
    return math.pi * r ** 2

def SqArea(side):
    return side ** 2

x = input("Input a positive number: ")

x = float(x)

if x < 0:
    print("Wrong Input")
    exit()


print("The area of the circle is %.2f" % CirArea(x))
print("The area of the square is %.2f" % SqArea(x))
