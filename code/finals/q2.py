stock = {
    'Mango': 50,
    'Durian': 50,
    'Pineapple': 50,
    'Banana': 50,
    'Watermelon': 50
}

price = {
    'Mango': 13,
    'Durian': 50,
    'Pineapple': 40,
    'Banana': 5,
    'Watermelon': 30
}

print("The items currently in stock along with their respective quantities: \n%s\n" % stock)

user_inputs = input("Input Fruit Items: ").split(',')

totalprice = 0

for inputs in user_inputs:
    fruit, amount = inputs.split()
    
    amount = int(amount)
    
    if fruit not in stock:
        print("Sorry, %s is not avaliable" % fruit)
        continue
    
    if amount > stock[fruit]:
        amount = 50
        
    stock[fruit] -= amount
    totalprice += price[fruit] * amount

print("\nThe overall amount due for your order = %d" % totalprice)
print("Here are the remaning items and their corresponding quantities: \n%s" % stock)
