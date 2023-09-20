sides = []

for i in ["a", "b", "c"]:
    sides.append(input("Input: %s=? " % i))


for i, values in enumerate(sides):
    if not values.isdigit():
        print("Some input is not a number")
        exit()
    else:
        sides[i] = int(sides[i])


print("Output: ", end="")

for i in sides:
    if i <= 0:
        print("Can't form a triangle")
        exit()

sides = sorted(sides, reverse=True)

if sides[0] < sides[1] + sides[2]:
    print("Form a triangle")
else: 
    print("Can't form a triangle")