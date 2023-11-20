amt = int(input("Please specify the amount of money you would like to withdraw: "))

five_hundred = amt // 500
one_hundred = amt % 500 // 100
fifty = amt % 500 % 100 // 50
two = amt % 500 % 100 % 50 // 2
one = amt % 500 % 100 % 50 % 2 

print("""we may give you: 
      %d bills(s) of 500 bath
      %d bills(s) of 100 bath
      %d bills(s) of 50 bath
      %d coin(s) of 2 bath
      %d coin(s) of 1 bath
      """ % (five_hundred, one_hundred, fifty, two, one))





