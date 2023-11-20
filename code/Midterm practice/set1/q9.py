speed = input("Enter speed in mph: ")
distance = input("Enter distance in miles: ")
format = input("Enter format (D or M): ")

if not speed.isdigit() or not distance.isdigit() or not format in ["D", "M"]:
    print("Invalid input")
    exit()
else:
    speed = int(speed)
    distance = int(distance)
    format = format.upper()

if speed <= 0 or distance <= 0:
    print("Invalid input")
    exit()

print("At %d mph, it will take" % speed)

if format == "D":
    print("%.2f hours to travel %d miles." % ((distance / speed), distance))

elif format == "M":
    print("%d hours and %d minutes to travel %d miles." % ((distance // speed), distance % speed * 60 // speed, distance))