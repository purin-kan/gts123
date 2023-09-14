print("Multiplication table:")
num = input("Please enter a number between 1 and 25: ")

if num.strip().isdigit() or num.strip().startswith("-") and num.strip()[1:].isdigit():
    if 1 <= int(num) <= 25:
        num = int(num)
    else:
        print("Number is out of range")
        exit()
else:
    print("not a number")
    exit()

print("Multiplication table of %d :" % num)

for i in range(1, 13):
    print("%d x %d = %d" % (num, i, num * i))