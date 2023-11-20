def TriArea(h, b):
    return 0.5 * h * b


h = input("Enter the height (h): ")
b = input("Enter the base (b): ")

try:
    h = float(h)
    b = float(b)
except ValueError:
    print("Invalid input")
    exit(0)
    
print("The area of the triangle is %.1f" % TriArea(h, b))
