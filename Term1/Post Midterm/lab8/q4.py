scores = {}

while True:
    user_input = input("Input (DONE = exit): ").split()

    if user_input[0] == "DONE":
        break
    
    if not user_input[0].isdigit() or not user_input[1].isdigit():
        print("Invalid input")
        continue
    
    if user_input[0] in scores.keys():
        print("Duplicated ID")
        continue
        
    scores[user_input[0]] = int(user_input[1])
    
for id, score in scores.items():
    print(id, score)
