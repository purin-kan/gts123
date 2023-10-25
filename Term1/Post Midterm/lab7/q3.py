size = int(input("Enter an integer number:"))

row = 0
while row < size:
    for col in range(size):
        if row == 0 or row == size - 1:
            print("o", end=' ')
        elif col == 0 or col == size - 1:
            print("o", end=' ')
        elif row <= col:
            print("x", end=' ')
        else:
            print(" ", end=" ")
    print()
    
    row += 1