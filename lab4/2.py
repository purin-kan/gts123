print("Fever Symptoms Advisor Program")
temp = float(input("Check your body temperature in F = "))
if (temp >= 100.4):
    print("you got a fever.")
    
    med = int(input("Choose your treatment : 1 = medication 2 = no medication >>> "))
    if (med == 1):
        print("Take Tylenol every 4 hours as needed")
    elif (med == 2):
        print("Taking a bath in lukewarm water or get the cool packs")
    else: 
        print("You chose the wrong choice")
    
else: 
    print("you are fine.")