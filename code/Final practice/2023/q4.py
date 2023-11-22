players = {}

while True:
    user_input = input("Input: ").split()
    
    if user_input[0] == 'done':
        break
    
    name = user_input[0]
    try:
        score = int(user_input[1])
    except ValueError:
        print("Invalid input")
        continue
    
    if score < 0:
        print("Invalid input")
        continue
    
    if name not in players:
        players[name] = score
    else:
        print("Duplicated player")
        continue
    

players = dict(sorted(players.items(), key=lambda x:x[1], reverse=True))

average = sum(players.values()) / len(players)
    
if not bool(players):
    print("No players")
    
for name, score in players.items():
    if score == max(players.values()):
        print(f"{name}\t{score}\tGold")
    elif score > average:
        print(f"{name}\t{score}\tSilver")
    else:
        print(f"{name}\t{score}")
