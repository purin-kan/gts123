while True:
    num = int(input("Enter an integer number:"))
    if not 0 < num <= 10:
        print("1 - 10 !!!!")
        continue
    
    for r in range(1, num + 1):
        for c in range(1, num + 1):
            if r >= c: 
                print(c, end=' ')
        print()
        
    for r in range(num - 1, 0, -1):
        for c in range(1, r + 1):
            print(c, end=' ')
        print()
