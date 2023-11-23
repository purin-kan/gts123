fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango', 'Kiwi']

for fruit in fruits:
    if len(fruit) >= 6:
        print(f"{fruit} is 6 characters or more!")
    else:
        print(f"{fruit} is only {len(fruit)} long!")