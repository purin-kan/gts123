import math

output = 0

a, b, c = input("Please enter an input: ").split("*")
option = input("Please enter your choice (1 or 2): ")

if not a.isdigit() or not b.isdigit() or not c.isdigit() or not option.isdigit():
    print("Invalid Inputs")
    exit()
else:
    a, b, c, option = int(a), int(b), int(c), int(option)

if a < 0 or b < 0 or c < 0 or not option in [1, 2]:
    print("Invalid Inputs")
    exit()


if option == 1:
    output = a + math.sqrt(b ** 2 + c ** 3)
if option == 2:
    output = int(str(a) + str(b)) % c

print("The output is %.2f" % output)
