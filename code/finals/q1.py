while True:
    money = input("Enter the initial deposit amount: ")
    
    try:
        money = float(money)
        
        if money < 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Please enter a positive number.")
        continue
    
    break
    
while True:
    interest_rate = input("Enter the annual interest rate: ")

    try:
        interest_rate = float(interest_rate)
        
        if interest_rate <= 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Please enter a positive number.")
        continue
    
    break

while True:
    years = input("Enter the number of years to save: ")
    
    try:
        years = int(years)
        
        if years < 0:
            print("Please enter a number greater than 0.")
            continue
    except ValueError:
        print("Please enter a number greater than 0.")
        continue
    
    break


print("-------------")
for i in range(1, years + 1):
    
    money = money * (1 + interest_rate / 100)
    print("Year %s: Total savings = %.2f" % (i, money))
    
print("\nAfter %s years, the total amount saved will be: %.2f" % (years, money))
