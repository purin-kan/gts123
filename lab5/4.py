num = input("Enter an integer number (n>0): ")

if num.isdigit():
    if int(num) <= 0:
        print("Number is out of range")
        exit()

    num = int(num)
else:
    print("not a number")
    exit()

print("(1) Factorial of n (n!)")
print("(2) Summation of n integers")

select = input("Select operation: ")

if select == "1":
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("%d! = %d" % (num, factorial))

elif select == "2":
    sum = 0

    for i in range(1, num + 1):
        sum += i

    print("the summation is %d." % sum)

else:
    print("N/A Operation!")
    exit()
