input = input("Input: ")

for i, num in enumerate(input):
    if input[i].isdigit():
        for i in range(int(input[i])): 
            if (i+1) % 3 == 0:
                print("#", end="")
            else:
                print("*", end="")
        print()
