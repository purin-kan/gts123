width, height = input("Input: ").split(" ")

if not width.isdigit() or not height.isdigit():
    print("Invalid Input")
    exit()
else:
    width = int(width)
    height = int(height)

if not 1 < width < 9 and not 1 < height < 9:
    print("Invalid Input")
    exit()


start = 1
end = width + 1

for r in range(1, height+1):
    if r % 2 != 0: # odd row
        for c in range(start, width + 1):
            print(c, end="")

        for i in range(1, start):
            print(i, end="")

        print()
        end -= 1

    else:  # even row
        for c in range(end, 0, -1):
            print(c, end="")

        for i in range(width, end, -1):
            print(i, end="")

        print()
        start += 1
