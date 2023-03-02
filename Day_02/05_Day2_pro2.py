# Description: Find the BMI of a person, such that the final answer is a whole number, (round it to the nearest whole number)

# Ask the user for their height (m) and weight (kg)
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Converting the dataTypes from str to floats
weight_as_float = float(weight)
squared_height_for_bmi_as_float = float(height) ** 2

# Calculate the value of the BMI
bmi = weight_as_float / squared_height_for_bmi_as_float

# Rounding the BMI to the nearest integer
# Using the int, here just removes everyone after the decimal place. (no rounding, just deleting everything after the decimal place.)
# rounded_bmi = int(bmi)
# This down below, however does round it effectively to the nearest integer.
rounded_bmi = round(bmi)

# printing out the result
print(rounded_bmi)

# Concepts used:
# 1. Type conversion 
# 2. Using the int() function to round numbers (inaccurately :P)
# 3. Using the the round() function to round numbers accurately