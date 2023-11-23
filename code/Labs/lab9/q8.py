def myRange(first_val, upper_bound, step_size):
    return list(range(first_val, upper_bound, step_size))


first = int(input("Enter the first number: "))
upper = int(input("Enter the upper bound: "))
step = int(input("Enter the step: "))

print("Range =", myRange(first, upper, step))
