lines = input("enter no. of lines: ")

if lines.strip().isdigit():
    lines = int(lines)
else:
    print("invalid input")
    exit()

for i in range(1, lines + 1):
    if i % 2 == 0:
        print("*" * i, end="")
    else:
        print("_" * i, end="")

    print()