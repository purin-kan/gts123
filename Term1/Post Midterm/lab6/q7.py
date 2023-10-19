import random

words = []

for i in range(4):
    temp = input("Enter string#%d: " % (i+1))
    words.append(temp.strip())
    
random.shuffle(words)

print("Random order of sentence: %s %s %s %s" % (words[0], words[1], words[2], words[3]))