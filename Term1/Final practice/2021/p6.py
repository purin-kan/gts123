sports = {}

while True:
    user_input = input("who plays what?")
    
    if user_input == "done":
        for sport, members in sports.items():
            print(f"{sport} is played by {members}")
        break
    
    user_input = user_input.split()
    input_sports = user_input[1].split(",")
    
    for sport in input_sports:
        if sport not in sports:
            sports[sport] = []
            
        sports[sport].append(user_input[0])
        