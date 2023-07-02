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
# > Python interprets the code line by line, and the order of the if-else statements does matter. Based on that fact, here are a few concise points for future reference:
# 1. In Python, the code is interpreted line by line, so the order of the if-else statements matters.
# 2. When evaluating the if-else statements, Python starts from the top and checks each condition sequentially.
# 3. If a condition is found to be true, Python executes the corresponding block of code and skips the rest of the if-else statements.
# 4. Therefore, in the given code example, only the first condition that evaluates to true will be executed, and the subsequent conditions will be ignored.
# 5. This is why the code works as expected, even though the descending conditions include the BMI range. Once a condition is met, the corresponding message is printed, and the program exits the if-else block.
# 6. It's important to order the if-else statements properly to handle the specific cases correctly, as Python does not automatically reorder the conditions based on the ranges.
