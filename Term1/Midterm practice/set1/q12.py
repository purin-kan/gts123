first = input("Give me a character: ")
second = input("Give me another character: ")

if not first.isalpha() and not second.isalpha():
    print("You need to input two characters.")
    exit()

alphabets = "abcdefghijklmnopqretuvwxyz"

firstIndex = -1
secondIndex = -1

for i in range(len(alphabets)):
    if alphabets[i] == first:
        firstIndex = i
    elif alphabets[i] == second:
        secondIndex = i

if firstIndex == -1 or secondIndex == -1:
    print("Invalid input")
    exit()

print("Output: ")
for i in range(firstIndex, secondIndex + 1):
    print(alphabets[i], end="")



