borrowed, duration, interest = input("Input: borrowed amount, duration(years), annual interest(%) ").split(" ")

if not borrowed.isdigit() or not duration.isdigit() or not interest.isdigit():
    print("Your input is invalid")
    exit()
else:
    borrowed = int(borrowed)
    duration = int(duration)
    interest = int(interest)

if borrowed < 0 or duration < 1 or interest < 0:
    print("Your input is invalid")
    exit()

pay = []

remaining = borrowed

for i in range(duration - 1):
    pay.append(int(input("Input: pay at the end of year %d " % (i + 1))))

    if pay[i] < remaining:
        remaining = (remaining - pay[i]) * (1 + interest / 100)
    else:
        print("You already cleared your loan")
        exit()

remaining = remaining * (1 + interest / 100)

print("Output: To clear you loan, you need to repay %.3f at the end of year %d" % (remaining, duration))
