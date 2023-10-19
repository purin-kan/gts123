dmy = input("Enter dd/mm/yyyy: ")

if len(dmy) != 8:
    print("Please enter 8 digits!!")
    exit()

if int(dmy[2:4]) > 12:
    print("Error! There're 12 months")
    exit()

print("Date = %s" % dmy[:2])
print("Month = %s" % int(dmy[2:4]))
print("Year = %s" % (int(dmy[4:]) - 543))

