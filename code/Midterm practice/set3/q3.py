import math

volume = input("Input a sphere volume: ")
input_unit = input("Input a unit of the volume : ")
output_unit = input("Input a unit of the sphere radius length: ")

try:
    volume = float(volume)
except ValueError:
    print("invalid volume")
    exit()

if volume < 0 or input_unit not in ["ft", "in"] or output_unit not in ["ft", "in"]:
    print("invalid input")
    exit()

converted_volume = volume

if input_unit == "ft" and output_unit == "in":
    converted_volume *= 12 ** 3
elif input_unit == "in" and output_unit == "ft":
    converted_volume /= 12 ** 3

radius = math.cbrt(converted_volume * 3 / 4 / math.pi)

print("The radius of a sphere with a volume of %.2f cubic %s is %.2f %s." % (volume, input_unit, radius, output_unit))

