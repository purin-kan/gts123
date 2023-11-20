namelist = ["Satawat", "Pisit", "Thanaphong", "Pished", "Nut", "Amon"]
print("student list: %s" % namelist)

while(input != 'q'):
    userinput = input("Please enter a student's name that you want to delete (q = exit): ")

    if userinput == 'q':
        break

    if userinput in namelist:
        comfirm = input("You will remove ' %s ' from this class.\nPlease type (Confirm 'y', Cancel 'n'): " % userinput)
        print()
        if comfirm == 'y':
            namelist.remove(userinput)
            print("student list: %s" % namelist)
        elif comfirm == 'n':
            print("student list: %s" % namelist)
            continue


