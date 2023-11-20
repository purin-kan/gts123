dna = input("DNA: ")
base = input("base: ")

times = 0

if not dna.isalpha() or not base.isalpha():
    print("This is not a DNA String")
    exit()

for i in dna:
    if not i in ["A", "T", "C", "G"]:
        print("This is not a DNA String")
        exit()


for i in dna:
    print("c: %s" % i)
    if i == base:
        print("True if test")
        times += 1

print("There are %d times that the base %s occur in this DNA" % (times, base))
