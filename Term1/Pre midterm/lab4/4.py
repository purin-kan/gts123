letter = input("Enter a single letter: ").capitalize()

if (letter == "A" or letter == "B" or letter == "C"):
    print("The digit 2 corresponds to the letter %s on the telephone" % letter)
elif (letter == "D" or letter == "E" or letter == "F"):
    print("The digit 3 corresponds to the letter %s on the telephone" % letter)
elif (letter == "G" or letter == "H" or letter == "I"):
    print("The digit 4 corresponds to the letter %s on the telephone" % letter)
elif (letter == "J" or letter == "K" or letter == "L"):
    print("The digit 5 corresponds to the letter %s on the telephone" % letter)
elif (letter == "M" or letter == "N" or letter == "O"):
    print("The digit 6 corresponds to the letter %s on the telephone" % letter)
elif (letter == "P" or letter == "R" or letter == "S"):
    print("The digit 7 corresponds to the letter %s on the telephone" % letter)
elif (letter == "T" or letter == "U" or letter == "V"):
    print("The digit 8 corresponds to the letter %s on the telephone" % letter)
elif (letter == "W" or letter == "X" or letter == "Y"):
    print("The digit 9 corresponds to the letter %s on the telephone" % letter)
    
else: 
    print("There is no digit on the telephone that corresponds to %s" % letter)
