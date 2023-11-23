A, B, C = [], [], []

num = int(input("how many people in a group? : "))

print("Please enter grade from group A")
for i in range(num):
    A.append(float(input("enter grade: ")))
print()

print("Please enter grade from group B")
for i in range(num):
    B.append(float(input("enter grade: ")))
print()

print("Please enter grade from group C")
for i in range(num):
    C.append(float(input("enter grade: ")))
print()

# A_high = A[0]
# for grade in A:
#     if grade > A_high:
#         A_high = grade

# B_high = B[0]
# for grade in B:
#     if grade > B_high:
#         B_high = grade

# C_high = C[0]
# for grade in C:
#     if grade > C_high:
#         C_high = grade
A_high = max(A)
B_high = max(B)
C_high = max(C)


print("the highest grade of group A is %.1f" % A_high)
print("the highest grade of group B is %.1f" % B_high)
print("the highest grade of group C is %.1f" % C_high)