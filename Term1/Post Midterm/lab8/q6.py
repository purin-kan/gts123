scores = {}

while True:
    user_input = input("Input (DONE = exit): ").split()

    if user_input[0] == "DONE":
        break
    
    if not all(map(str.isdigit, user_input)):
        print("Invalid input")
        continue
    
    if user_input[0] in scores:
        scores[user_input[0]] = max(scores[user_input[0]], int(user_input[1]))
    else:
        scores[user_input[0]] = int(user_input[1])
    
for id, score in scores.items():
    print(id, score)