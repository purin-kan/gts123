primes = []

while True:
    is_prime = True
    
    user_input = input("Enter a number ")
    
    if user_input == "done":
        print("The sum of all primes is ", sum(primes))
        break
    
    
    for i in range(2, int(user_input)):
        if int(user_input) % i == 0:
            print("It is not a prime")
            is_prime = False
            break

    if is_prime:
        print("It is a prime")
        primes.append(int(user_input))
