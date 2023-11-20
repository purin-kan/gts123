sentence = input("Input a sentence: ")

words = sentence.lower().split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

found_repeated = False
print("Output:")
for word, count in freq.items():
    if count > 1:
        print(word)
        found_repeated = True

if not found_repeated:
    print("none")



# # * Alternative Solution
# sentence = input("Input a sentence: ")

# words = sentence.lower().split()

# unique_words = set(words)
# repeated_words = set()

# for word in words:
#     if word in unique_words:
#         unique_words.remove(word)
#     else:
#         repeated_words.add(word)


# print("Output:")
# if len(repeated_words) > 0:
#     for word in sorted(repeated_words):
#         print(word)
# else:
#     print("none")
    