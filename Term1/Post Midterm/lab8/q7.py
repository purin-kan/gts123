seq1 = input("Input sequence1: ").split()
seq2 = input("Input sequence2: ").split()

set1 = set(filter(str.isdigit, seq1))
set2 = set(filter(str.isdigit, seq2))

print("Output:", bool(set1 & set2))