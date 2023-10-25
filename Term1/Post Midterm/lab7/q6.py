while True:
    print("===== MAIN MENU =====\n1. Addition\n2. Subtraction\n3. Exit\n")

    choice = int(input("Select an operation (1-3): "))
    if choice == 1:
        numbers = input("Enter two numbers: ").split()
        print(f"{numbers[0]} + {numbers[1]} = {int(numbers[0]) + int(numbers[1])}\n\n")
    elif choice == 2:
        numbers = input("Enter two numbers: ").split()
        print(f"{numbers[0]} - {numbers[1]} = {int(numbers[0]) - int(numbers[1])}\n\n")
    elif choice == 3:
        break
    
print("Bye!!!")