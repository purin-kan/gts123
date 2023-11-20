height = int(input("Height: "))

if height == 0:
    print("Height must be greater than 0")
    exit()

for i in range(1, height + 1):
    print("#" * (height - i), end="")
    print("*" * (i * 2 - 1), end="")
    print("#" * (height - i))