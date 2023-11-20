numbers = []

print("===================\nCashier Program\n===================\n")

while True:
    num = float(input("Enter item price or -1 when finished: "))
    
    if num == -1:
        break
    
    numbers.append(num)
    
print(f"\nTotal purchase amount is {sum(numbers)}")

payment = int(input("\nYour payment: "))

print(f"\nYou bought {len(numbers)} items today.")
print("Your change is %.2f baht." % (payment - sum(numbers)))
