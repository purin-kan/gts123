size = input("Input: ")

if not size.isdigit():
    print("Your input is invalid")
    exit()
else:
    size = int(size)

if size < 3:
    print("Your input is invalid")
    exit()

# for higher end
for highR in range(size):
    for leftC in range(size):
        if leftC <= highR and (leftC % 2) == 0:
            print("*", end="")
        elif leftC <= highR and (leftC % 2) != 0:
            print("0", end="")
        else:
            print(" ", end="")
    for rightC in range(size):
        if size - rightC - 1 <= highR and (rightC % 2) == 0:
            print("*", end="")
        elif size - rightC - 1 <= highR and (rightC % 2) != 0:
            print("0", end="")
        else:
            print(" ", end="")
    print()

# for lower end
for lowR in range(size - 1):
    for leftC in range(size):
        if size - leftC - 1 <= lowR:
            print(" ", end="")
        elif (leftC % 2) != 0:
            print("0", end="")
        else:
            print("*", end="")
    for rightC in range(size):
        if rightC <= lowR:
            print(" ", end="")
        elif (rightC % 2) != 0:
            print("0", end="")
        else:
            print("*", end="")
    print()
