# statements


# library


# input
weight = float(input("Input the weight in kilograms: "))
height = float(input("Input the height in meters: "))

# processing
BMI = weight/height**2

# output
if 0 <= BMI < 18.5:
    print(f"BMI: {BMI:.2f}; Classification: Below the weight.")
elif 18.5 <= BMI <= 25:
    print(f"BMI: {BMI:.2f}; Classification: Ideal weight.")
elif 25 < BMI <= 30:
    print(f"BMI: {BMI:.2f}; Classification: Overweight.")
elif 30 <= BMI <= 40:
    print(f"BMI: {BMI:.2f}; Classification: Obesity.")
elif 40 < BMI:
    print(f"BMI: {BMI:.2f}; Classification: Morbid Obesity.")
else:
    print(f"ERROR! No such classification exists.")

input()