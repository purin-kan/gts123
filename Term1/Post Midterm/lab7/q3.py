size = int(input("Enter an integer number:"))

row = 1
while row <= size:
    for col in range(size):
        if row == 1 or row == size:
            print("o", end=' ')
        elif col == 0 or col == size - 1:
            print("o", end=' ')
        elif row <= col + 1:
            print("x", end=' ')
        else:
            print(" ", end=" ")
    print()
    
    row += 1