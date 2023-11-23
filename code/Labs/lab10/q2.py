import numpy as np

leftMatrix = np.zeros([3, 3])
rightMatrix = np.zeros([3, 1])

inputC = 1
r = 0
c = 0
while inputC <= 12:
        while True:
            try: 
                temp = int(input(f"Input C{inputC}: "))
                break
            except ValueError:
                print("Invalid input")
                
        if inputC % 4 == 0:
            rightMatrix[inputC//4 - 1][0] = temp
        else:
            if c == 3:
                c = 0
                r += 1
            leftMatrix[r][c] = temp
            c += 1
                    
        inputC += 1

        
try:
    inverse = np.linalg.inv(leftMatrix)
except:
    print("Unable to find a solution")
    exit()
    
solution = np.matmul(inverse, rightMatrix)


print("""Solution:
      x = %.2f
      y = %.2f
      z = %.2f""" % (solution[0][0], solution[1][0], solution[2][0]))
