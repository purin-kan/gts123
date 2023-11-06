print("========Welcome to Hi!! Car Wash========")

service_type = input("Choose your services: W=Wash C=Wash+Vacuum :").capitalize()
car_size = input('Enter car size: "S", "M", "L" : ').capitalize()

price = 0

# Check car size
if car_size == "S":
    if service_type == "W":
        price = 100
    elif service_type == "C":
        price = 120
    else:
        print("Invalid service type. Please enter 'W' or 'C'.")

elif car_size == "M":
    if service_type == "W":
        price = 120
    elif service_type == "C":
        price = 140
    else:
        print("Invalid service type. Please enter 'W' or 'C'.")

elif car_size == "L":
    if service_type == "W":
        price = 140
    elif service_type == "C":
        price = 160
    else:
        print("Invalid service type. Please enter 'W' or 'C'.")

else:
    print("Invalid car size. Please enter 'S', 'M', or 'L'.")

if price > 0:
    print(f"Price = {price} baht")
