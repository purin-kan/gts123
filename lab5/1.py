even = 0
odd = 0

for i in range(5):
    temp = input("enter a number: ")
    if temp.strip().isdigit():
        if int(temp) % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        print("not a number")
        exit()

print("there were %d even numbers" % even)
print("there were %d odd numbers" % odd)
