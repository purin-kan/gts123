from itertools import permutations

input_list = input("Enter a comma-separated list: ").split(",")
if len(input_list) >= 3:
    permutations_list = list(permutations(input_list, 3))
    for perm in permutations_list:
        print(" ".join(perm))
else:
    print("List must contain at least 3 elements.")