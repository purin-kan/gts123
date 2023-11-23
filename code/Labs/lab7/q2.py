names = []

while True:
    name = input("Input: Enter a word:")
    if name == "exit":
        break
    names.append(name.capitalize())

print("Output:", names)