# Program Description: Create a program using the operators and f-Strings, that tells us how many days, weeks, and months we have left if we live till the age of 90 years. (make sure to round the end results)

# Declaration:
# 1 year = 365 days = 52 weeks = 12 months

# Storing 90 in a variable
death_year = 90

# Calculating the days, weeks and months in 90 years
death_year_days = death_year * 365
death_year_weeks = death_year * 52
death_year_months = death_year * 12

# Asking the current age of the user
age = input("What is your current age? ")

# Converting age to float
age_as_float = float(age)

# Calculating the days, weeks and months of the user's current age:
current_age_in_days = age_as_float * 365
current_age_in_weeks = age_as_float * 52
current_age_in_months = age_as_float * 12

# Calculating life left in days, weeks, and months:
life_left_days = death_year_days - current_age_in_days
life_left_weeks = death_year_weeks - current_age_in_weeks
life_left_months = death_year_months - current_age_in_months

# Results:
print(f"You have {round(life_left_days)} days, {round(life_left_weeks)} weeks and {round(life_left_months)} months left.")

# Feedback:
# 1. Good job, the output is exactly as expected but the code could be a little more polished as it has some redundant lines of code.
# 2. Instead of converting both the death age & the current age to days, weeks, and months to perform operations on them the whole process could be reduced down to this:
# 3. Subtract the current age from the death age and then convert the answer into days, weeks and months.