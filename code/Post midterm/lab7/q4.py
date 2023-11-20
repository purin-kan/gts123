size = int(input("Enter an integer number:"))

row = 1
while row <= size:
    for c in range(size):
        if row == 1 or row == size:
            print("x", end=' ')
        elif c == 0 or c == size - 1:
            print("x", end=' ')
        else:
            print(" ", end=" ")
    print()
    
    row += 1