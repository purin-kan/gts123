import random

width = input("Rectangle width: ")
height = input("Rectangle height: ")
thickness = input("Rectangle thickness: ")

border_characters = "#*$"

if not width.isdigit() and not height.isdigit() and not thickness.isdigit():
    print("Invalid input")
    exit()

width = int(width)
height = int(height)
thickness = int(thickness)

if width <= 0 or height <= 0 or thickness <= 0:
    print("Invalid input")
    exit()

for r in range(height):
    for c in range(width):
        if r in range(0, thickness) or r in range(height-thickness, height):
            print(random.choice(border_characters), end="")
        elif c in range(0, thickness) or c in range(width-thickness, width):
            print(random.choice(border_characters), end="")
            c += 1
        else:
            print(" ", end="")
            c += 1
    print()
