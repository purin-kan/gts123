import numpy as np

height = float(input("Enter the pentagon height: "))

side = (2 * height) / (np.sqrt(5 + 2 * np.sqrt(5)))
area = (side ** 2) * np.sqrt(25 + 10 * np.sqrt(5)) / 4
perimeter = side * 5

print("The length for one side of the pentagon is %.4f." % (side))
print("The pentagon area and perimeter are %0.4f and %0.4f." % (area, perimeter))