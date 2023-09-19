h, m, s = input("Input: ").split(":")

if h.isdigit() and m.isdigit() and s.isdigit():
    h = int(h)
    m = int(m)
    s = int(s)
    
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        sec = h * 3600 + m * 60 + s
        
        print("The number of seconds = %d" % sec)
    
    else: 
        print("Invalid time")
        exit()
    
else: 
    print("Invalid time")
    exit()
