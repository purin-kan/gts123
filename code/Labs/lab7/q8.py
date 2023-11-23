even = 0
odd = 0


while True:
    num = int(input("Enter an integer (0 to exit) : "))
    
    if num == 0:
        break
    
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    
print("---------------------------------- ")
print("The number of even integers is %d." % even)
print("The number of odd integers is %d." % odd)