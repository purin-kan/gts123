days = int(input("Input number of days: "))
hours = int(input("Input number of hours: "))

choice = int(input("""Please select a choice: 
      1-to calculate the total number of seconds or
      2-to calculate the total number of minutes: 
      Enter your salected choice: """))

print("\n-----------------------------------------------")

if (choice == 1):
    print("The total number of seconds are %d." % ((days * 24 + hours) * 60 * 60))
    
elif (choice == 2):
    print("The total number of minutes are %d." % ((days * 24 + hours) * 60))