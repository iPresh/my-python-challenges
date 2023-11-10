
weight = float(input("what is your weight in kilograms?"))
height = float(input("what is your height in meters?"))

BMI = weight / height ** 2

BMI = round(BMI, 1)

print(f"The body mass index is: {BMI}")

print("\n------BMI Categories------")

print("<18.5        : Underweight")
print("18.5 – 24.9  : Normal weight")
print("25 - 29.9    : Underweight")
print(">=30         : Obesity")
