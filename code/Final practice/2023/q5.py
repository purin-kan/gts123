while True:
    num = int(input("Enter an integer number (0 to exit): "))
    
    if num == 0:
        print("Exit program. Bye!")
        exit()
        
    if not 0 < num <= 9:
        print("Valid value is between 0 and 9!")
        exit()
    
    
    for i in range(num, 0, -1):
        print(' ' * (i - 1) + (str(num) + ' ') * (num - i + 1))
