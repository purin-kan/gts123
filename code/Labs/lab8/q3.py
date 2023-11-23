seq1 = input("Input sequence1: ").split()
seq2 = input("Input sequence2: ").split()

set1 = set()
set2 = set()

for i in seq1:
    if i.isdigit():
        set1.add(i)

for j in seq2:
    if j.isdigit():
        set2.add(j)

if set1 == set2:
    print("Output: same set")
else:
    print("Output: different set")
