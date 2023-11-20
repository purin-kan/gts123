import math

ans = 0

values = input("Please enter two integers: ").split(" ")

if not values[0].isdigit() and not values[1].isdigit():
    print("Invalid input")
    exit()
    

if int(values[0]) > int(values[1]):
    b = int(values[0])
    a = int(values[1])
else:
    b = int(values[1])
    a = int(values[0])
        

for i in range(a, b+1):
    ans += i
    
ans = math.sqrt(ans)

        
print("The minimum number is %d" % a)
print("The maximum number is %d" % b)
print("The square root of the summation is %.2f" % ans)
