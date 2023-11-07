while True:
    userInput = input("Input initial money and interest rate: ").split()

    if userInput[0] == "exit":
        break
    
    if not all(map(lambda x: x.replace('.', '', 1).isdigit() and float(x) >= 0, userInput)):
        print("Invalid input, please try again.")
        continue
    
    if not all(map(lambda x: (float(x)) > 0, userInput)):
        print("Invalid input, please try again.")
        continue
    
    
    money = float(userInput[0])
    interestRate = float(userInput[1]) / 100
    
    for year in range(1, 6):
        
        interest = money * interestRate
        
        print("YEAR %d --- %.2f + %.2f = %.2f" % (year, money, interest, money + interest))
        
        money += interest
    
    print("*****")
    