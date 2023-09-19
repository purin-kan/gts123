a, b, c = input("a, b, c = ").split(" ")

if a not in ['True', 'False'] or b not in ['True', 'False'] or c not in ['True', 'False']:
    print("Invalid input")
    exit()

if a == 'True':
    a = True
else:
    a = False
if b == 'True':
    b = True
else:
    b = False
if c == 'True':
    c = True
else:
    c = False
    
if not a and not b and not c : 
    print("Grant")
    
elif a:
    print("Grant")
    
else: 
    print("Deny")
