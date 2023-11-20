while True:
    
    num = input("Enter an integer number ('X' to exit) : ")

    if num in 'Xx':
        break

    if num.isdigit():
        num = int(num)
        
        for r in range(num):
            for c in range(num):
                if r == c or r + c == num - 1:
                    print('X', end=' ')
                else: 
                    print('.', end=' ')
            print()

    else: 
        continue
