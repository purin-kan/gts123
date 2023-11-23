sentence = input("Input: ")

words = sentence.lower().split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

max_freq = max(freq.values())

print("Output:")
for word, count in freq.items():
    if count == max_freq:
        print(word, "=", count)
