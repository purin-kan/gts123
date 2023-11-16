import numpy as np

def receiveInput(point):
    while True:
        try:
            point = input(f"Input coordinate of {point}: ").split()
            point = list(map(int, point))
            break
        except ValueError:
            print("error, retry...")
            
    return np.array(point, dtype=int)

def findDistance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)


p1 = receiveInput("P1")
p2 = receiveInput("P2")
p3 = receiveInput("P3")

d12 = findDistance(p1, p2)
d23 = findDistance(p2, p3)
d31 = findDistance(p3, p1)

results = np.array([d12, d23, d31])

print("Output: \nThe longest distance = %.2f" % np.max(results))
