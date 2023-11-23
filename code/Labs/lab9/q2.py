def LeftRotate():
    global x
    global n
    return x[n:] + x[:n]
    
def RightRotate():
    global x
    global n
    return x[-n:] + x[:-n] # type: ignore


x = input("Enter 5 inputs: ").split()
n = input("Enter an integer number of rotations (0-4): ")

try:
    n = int(n)
    
except ValueError:
    print("Error!")
    exit()

if not 0 <= n <= 4:
    print("Error!")
    exit()

print("The Left-rotated list:", LeftRotate())

print("The Right-rotated list:", RightRotate())
