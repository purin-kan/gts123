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

for h in range(height):
    if h < thickness or h >= height - thickness:
        for i in range(width):
            print(random.choice(border_characters), end="")
        print()
    else:
        for w in range(width):
            if w < thickness or w >= width - thickness:
                print(random.choice(border_characters), end="")
            else:
                print(" ", end="")
        print()
