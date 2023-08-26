chocolate = int(input("Enter amount of melted chocolate to be poured into the cup (ml): "))
milk = int(input("Enter amount of milk to be poured into the cup (ml): "))

print("Now Emmy's cup is filled with %.2f ml (or about %.2f oz) of chocolate milk." % (chocolate + milk, (chocolate + milk) * 0.0338))