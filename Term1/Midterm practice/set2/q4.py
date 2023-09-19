specialChar = input("Enter a special character: ")
size = int(input("Enter the size of the pattern: "))
pattern = int(input("Enter option for the pattern: "))

if size < 0 or not pattern in [1, 2] or not specialChar in ['#', '$', '@', '*', '^']:
    print("Wrong input values")
    exit()
    
for c in range(size):
    if pattern == 1:
        specialIndex = 0
    
        for r in range(size):
            if c == specialIndex:
                print("%s " % specialChar, end="")
            else: 
                print(". ", end="")
                
            specialIndex += 1
        print()
        
    else:
        specialIndex = size - 1
        
        for r in range(size):
            
            if c == specialIndex:
                print("%s " % specialChar, end="")
            else: 
                print(". ", end="")
                
            specialIndex -= 1
        print()