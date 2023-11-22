votes = {}

while True: 
    user_input = input("Input: ")
    
    if user_input == "done":
        break
    
    try:
        user_input = int(user_input)
        
        if not 1 <= user_input <= 1000:
            print("ERROR")
            continue
    except ValueError:
        print("ERROR")
        continue
    
    if user_input not in votes:
        votes[user_input] = 1
    else: 
        votes[user_input] += 1
    
    
votes = dict(sorted(votes.items()))
    
print("----SUMMARY----")
if not votes:
    print("The list is empty")
else:
    for candidate, vote in votes.items():
        print("%s %d" % (candidate, vote)) 
