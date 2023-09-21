input = input ("Input: ")

if len(input) != 3:
    print("Only three characters are allowed.")
    exit()
else:
    input = input.upper()
    
for i in range(len(input)):
    if input[i] not in ["A", "E", "I", "O", "U"]:
        print('Invalid input, valid characters: ["A", "E", "I", "O", "U"]')
        exit()

start = 0

for j in range(6):
    for k in range(start, 3):
        print(input[k], end="")
    for l in range(2, start-1, -1):
        print(input[l], end="")
    print()
    start += 1
 

    
# 012
# 021
# 102
# 120
# 201
# 210
