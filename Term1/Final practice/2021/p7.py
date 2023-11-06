import math

while True:
    user_input = input("Input radius and height: ").split()
    
    if user_input[0] == "done":
        break
    
    try:
        radius = float(user_input[0])
        height = float(user_input[1])
    except ValueError:
        print("Invalid inputs")
        continue
    
    if radius < 0 or height < 0:
        print("Invalid inputs")
        continue
    
    volume = math.pi * radius**2 * height
    print("The cylinder volume is %.2f" % volume)