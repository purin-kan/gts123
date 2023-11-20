input = input ("Input: ")

if len(input) != 3:
    print("Only three characters are allowed.")
    exit()
else:
    input = input.upper()
    
for i in range(len(input)):
    if input[i] not in "AEIOU":
        print('Invalid input, valid characters: ["A", "E", "I", "O", "U"]')
        exit()

for vowel in input:
    x = input.replace(vowel, "")
    for i in x:
        y = x.replace(i, "")
        print("%s%s%s" % (vowel, i, y))
        