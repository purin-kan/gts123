size = input("Input: ")

if not size.isdigit():
    print("Your input is invalid")
    exit()
else:
    size = int(size)

if size < 3:
    print("Your input is invalid")
    exit()
