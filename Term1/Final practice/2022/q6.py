accounts = {}

def deposit(account, amount):
    accounts[account] += amount
    
def withdraw(account, amount):
    if accounts[account] < amount:
        print("You don't have enough amount.")
    else:
        accounts[account] -= amount

while True:
    account = input("Open bank account with initial amount (account number, amount): ").split()
    
    if account[0] == "done":
        break
    
    if account[0] not in accounts:
        accounts[account[0]] = float(account[1])
            
        
while True:
    transaction = input("Enter transaction (account number, withdraw/deposit, amount): ").split()
    
    if transaction[0] == "done":
        break
    
    if transaction[0] not in accounts:
        print("Invalid account. Please enter transaction again")
        continue 
    
    if transaction[1] == 'w':
        withdraw(transaction[0], float(transaction[2]))
    elif transaction[1] == 'd':
        deposit(transaction[0], float(transaction[2]))
        
    print("Avaliable transaction amount of account number %s is %.2f" % (transaction[0], accounts[transaction[0]]))
    