user_inputs = input("Integer inputs: ").split()

user_inputs = list(filter(lambda x: x.isdigit(), user_inputs))
user_inputs = sorted(user_inputs, key=lambda x: int(x[-1]))

groups = {}

for user_input in user_inputs:
    if user_input[-1:] not in groups:
        groups[user_input[-1:]] = []
        
    groups[user_input[-1:]].append(user_input)

for group, members in groups.items():
    print(f"Group {group}, Total {len(members)}, Values: {members}")
