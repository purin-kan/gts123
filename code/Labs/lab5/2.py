sum = 0

for i in range(1, 6):
    temp = input("enter an integer #%d: " % i)
    if temp.strip().isdigit() or temp.strip().startswith("-") and temp.strip()[1:].isdigit():
        sum += int(temp)
    else:
        print("not a number")
        exit()

print("the summation is %d." % sum)