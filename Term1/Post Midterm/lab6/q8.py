userinput = input("Enter a string: ")

for letter in userinput:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")