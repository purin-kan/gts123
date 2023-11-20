inputs = []

for i in range(5):
    user_input = input("Input#%d : " % (i+1))
    inputs.append(int(user_input))

choice = int(input("Select the option: 1) Summary, 2) average, 3) min, 4) max ...."))

if choice == 1:
    ans = sum(inputs)
elif choice == 2:
    ans = sum(inputs) / len(inputs)
elif choice == 3:
    min = inputs[0]
    for i in inputs:
        if i < min:
            min = i
    ans = min
elif choice == 4:
    max = inputs[0]
    for i in inputs:
        if i > max:
            max = i
    ans = max
else:
    ans = 0
    
print("Your result is %d" % ans)