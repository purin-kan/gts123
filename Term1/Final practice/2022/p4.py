while True:
    userInput = input("Input x,y,z :").split(",")

    if userInput[0].lower() == "exit":
        print("Program ended.")
        break

    if not all(map(lambda x: x.replace('.', '', 1).isdigit() and float(x) >= 0, userInput)):
        print("Invalid input.")
        continue
    
    if len(userInput) != 3:
        print("Enter 3 values.")
        continue
    
    map(lambda x: int(x), userInput)
    
    volume = (1/3) * ((1/2) * float(userInput[0]) * float(userInput[1])) * float(userInput[2])
    print("Volume of Tetrahedron is %.2f cubic unit." % volume)
