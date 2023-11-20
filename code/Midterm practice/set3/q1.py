import math

diameter = input("Input a circle diameter: ")
input_unit = input("Input a unit of the diameter: ")
output_unit = input("Input a unit of the output area: ")

try:
    diameter = float(diameter)
except TypeError:
    print("invalid diameter")

if diameter < 0 or input_unit not in ["mm", "cm", "in"] or output_unit not in ["mm", "cm", "in"]:
    print("invalid input")
    exit()

if input_unit != output_unit:
    if input_unit == "mm" and output_unit == "cm":
        diameter /= 10
    elif input_unit == "mm" and output_unit == "in":
        diameter /= 25.4
    elif input_unit == "cm" and output_unit == "in":
        diameter /= 2.54
    elif input_unit == "cm" and output_unit == "mm":
        diameter *= 10
    elif input_unit == "in" and output_unit == "mm":
        diameter *= 25.4
    elif input_unit == "in" and output_unit == "cm":
        diameter *= 2.54


area = math.pi * (diameter / 2) ** 2

print("The surface of a circle with a %.2f %s in diameter is %.2f square %s." % (diameter, input_unit, area, output_unit))
