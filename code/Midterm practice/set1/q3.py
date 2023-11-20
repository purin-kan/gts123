customer = input("Input (Number of customers): ")
discountCode = input("Input (Discount code): ")

price = 0
discount = 0

if customer.isdigit():
    customer = int(customer) 
else:
    exit()

if customer < 0:   
    print("Invalid number of customers")
    exit()

if 1 <= customer <= 3:
    perPerson = 399
elif 4 <= customer <= 6:
    perPerson = 499
else: 
    perPerson = 599

price += customer * perPerson


discountCode = discountCode.upper()    
if discountCode == "CASH":
    discount = 5
elif discountCode == "BIRTHDAY":
    discount = 10
elif discountCode == "COVID":
    discount = 30
    
print("%d person x %.2f" % (customer, perPerson))
print("A subtotal price is %.2f baht" % price)
print("On-top discount %d%%" % discount)
print("A total price is %.2f baht" % (price * (1 - discount / 100)))