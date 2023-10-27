sequence = input("Input: ").split()

freq = {}
for element in sequence:
    if element.isdigit():
        freq[element] = freq.get(element, 0) + 1

good_sequence = True

for element, count in freq.items():
    if int(element) != count:
        good_sequence = False

print("Output: ", end='')
if good_sequence: 
    print("good sequence")
else: 
    print("not good sequence")

sequence = input("Input: ").split()
