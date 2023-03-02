# Program Description: Create a program using the operators and f-Strings, that tells us how many days, weeks, and months we have left if we live till the age of 90 years. (make sure to round the end results)

# Declaration:
# 1 year = 365 days = 52 weeks = 12 months

# Storing 90 in a variable
death_year = 90

# Asking the current age of the user
age = input("What is your current age? ")

# Converting age to float
age_as_float = float(age)

# Calculating age left in years
age_left = death_year - age_as_float

# Calculating age left in days, weeks, and months
age_left_in_days = age_left * 365
age_left_in_weeks = age_left * 52
age_left_in_months = age_left * 12

# Results:
print(f"You have {round(age_left_in_days)} days, {round(age_left_in_weeks)} weeks and {round(age_left_in_months)} months left.")

# Feedback:
# 1. Good job, the output is exactly as expected but the code could be a little more polished as it has some redundant lines of code.
# 2. Instead of converting both the death age & the current age to days, weeks, and months to perform operations on them the whole process could be reduced down to this:
# 3. Subtract the current age from the death age and then convert the answer into days, weeks and months.