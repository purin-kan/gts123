inputs = []

for i in range(9):
    user_input = input("Input: ")
    
    if user_input not in ['x', 'o']:
        print("Wrong input")
        exit()
        
    inputs.append(user_input)
    
print("--------")
for i in range(3):
    print("|%s|%s|%s|" % (inputs[3*i], inputs[3*i+1], inputs[3*i+2]))
    print("--------")
