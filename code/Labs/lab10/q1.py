import numpy as np

while True:
    try:
        size = int(input("Input size of matrix: "))
        break    
    except ValueError:
        print("Invalid input")
        
matrix = np.identity(size)

for r in range(size):
    for c in range(size):
        matrix[r][c] = input(f"Input element at row {r+1} column {c+1}: ")
        
        
inverse = np.linalg.inv(matrix)
determinant = np.linalg.det(matrix)

print("Output: ")
print("Matrix = \n", matrix)
print("Determinant =", determinant)
print("Inverse Matrix = \n", inverse)
