points = 100

while True:
    user_input = input("Command: ").split()
    
    command = user_input[0]
    number = int(user_input[1])
    
    if command == "done" and number == 0:
        break
    
    if command not in ['P', 'R'] or number < 0:
        print("Invalid command!")
        continue
    
    if command == 'P':
        points += number // 50
        print("You earned %d points" % (number // 50))
        print("Your accumulated points = %d points" % (points))
        
    elif command == 'R':
        if number > points:
            print("Not enough points")
            continue
        points -= number
        print("You redeemed %d points" % (number))
        print("Your accumulated points = %d points" % (points))
