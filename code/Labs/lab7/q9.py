numbers = []

while True:
    num = int(input("Enter an integer (-1 to exit) : "))
    
    if num == -1:
        break
    
    numbers.append(num)
    
print("The sum of %d number(s) is %d." % (len(numbers), sum(numbers)))