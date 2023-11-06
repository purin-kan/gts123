numbers = []

while True:
    user_input = input("Input: ")
    
    if user_input == "done":
        
        if len(numbers) < 3:
            print("Not enough inputs")
            break
        
        numbers.sort()
        
        print("The highest sumand the smallest sum are %d and %d." % (sum(numbers[0:2]), sum(numbers[-3:])))
        break
    
    try:
        user_input = int(user_input)
        
    except ValueError:
        print("Invalid input")
        continue

    numbers.append(user_input)
    