from itertools import combinations

input_list = input("Enter a comma-separated list: ").split(",")
if len(input_list) >= 3:
    combinations_list = list(combinations(input_list, 3))
    for comb in combinations_list:
        print(" ".join(comb))
else:
    print("List must contain at least 3 elements.")
    