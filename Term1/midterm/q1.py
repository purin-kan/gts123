minute, second = input("Enter your running pace (minutes per kilometer): ").split(":")
distance = input("Enter your distance (a) Mini-marathon, (b) Half-marathon, (c) Full-marathon: ")

minute, second = int(minute), int(second)
distance = distance.upper()

finishtime = 0
cutoff = 0
pace = minute + second/60

if distance == "A":
    distance = 10
    cutoff = 2.5
    finishtime = pace * distance
elif distance == "B":
    distance = 21.0975
    cutoff = 4
    finishtime = pace * distance
elif distance == "C":
    distance = 42.195
    cutoff = 6
    finishtime = pace * distance
else:
    print("Invalid distance selection")
    exit()
    
finishtime /= 60

print("Your estimated finish time is %d hours %d minutes" % (finishtime // 1, (finishtime % 1) * 60))

if finishtime < cutoff:
    print("You can finish in cutoff time (Your cutoff time is %.2f hours)." % cutoff)
else: 
    print("You cannot finish in cutoff time (Your cutoff time is %.2f hours)." % cutoff)