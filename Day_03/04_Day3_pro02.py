# Program Description: Make a BMI calculator (V.02), this should be an upgrade to the previous version, such that upon calculating the BMI, it tells the user whether they are underweight, healthy, overweight, obese or clinically obese.

# Asking the user to enter their height and weight:
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculating the BMI:
bmi = round(weight / height ** 2)

# Calculating the weight categories:
if bmi <= 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi <= 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi <= 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi <= 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")

# Observation:
# 1. 