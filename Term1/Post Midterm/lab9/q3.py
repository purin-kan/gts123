xList = []

def UserInput():
    while True:
        temp = input("Enter an input: ")
        
        if temp == "Done":
            break
        
        try:
            temp = int(temp)
        except ValueError:
            print("Error!")
            exit()
    
        if temp < 0:
            print("Error!")
            exit()
        
        global xList
        xList.append(temp)    
        
def SumOut():
    global xList
    return sum(xList)

def MinOut():
    global xList
    return min(xList)

def MaxOut():
    global xList
    return max(xList)


UserInput()
print()
print("The summation is", SumOut())
print("The minimum is", MinOut())
print("The maximum is", MaxOut())
