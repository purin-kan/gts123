fourdigit = int(input("Enter a four-digit integer: "))

firsttwo = fourdigit // 100
lasttwo = fourdigit % 100

print("The result of %d + %d = %d" % (firsttwo, lasttwo, firsttwo + lasttwo))
print("The result of %d - %d = %d" % (firsttwo, lasttwo, firsttwo - lasttwo))
print("The integer value of  %d/%d = %d" % (firsttwo, lasttwo, firsttwo//lasttwo))
print("The remainder of  %d/%d = %d" % (firsttwo, lasttwo, firsttwo%lasttwo))
