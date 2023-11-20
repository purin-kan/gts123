weight = 0
height = 0
UserBMI = 0

def UserInput():
    global weight
    global height
    
    weight = float(input("Input your weight (kilogram): "))
    height = float(input("Input your height (meter): "))
    
def FindBMI(hh, ww):
    global UserBMI
    UserBMI = ww / (hh ** 2)
    
def ShowBMI(MyBMI):
    print("The user BMI is %.2f" % MyBMI)
    
UserInput()
FindBMI(height, weight)
ShowBMI(UserBMI)
