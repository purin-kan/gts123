input = input("Please enter your information: ").split(",")


if input[0].isalpha() and input[1].isdigit():
    name = input[0]
    age = int(input[1])
    
elif input[1].isalpha() and input[0].isdigit(): 
    name = input[1]
    age = int(input[0])
else: 
    print("Please enter your complete information.")
    exit()


if 0 <= age <= 120:
    print("Your name is %s\nYour age is %d" % (name, age))
    
else: 
    print("Please enter your complete information.")