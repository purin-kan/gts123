def CelciusToFahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Enter temperature in degree Celcius: "))
print("The degree in Fahrenheit is %.2f" % CelciusToFahrenheit(c))
