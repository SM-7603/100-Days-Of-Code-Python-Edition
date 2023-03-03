# Program Description: The program should ask the total bill, the percentage of tip to be given and the number of people to split the bill between. The final amount must be rounded off till 2 decimal places.

# Greeting message
print("Welcome to the tip calculator!")

# Asking the user for the total bill
total_bill = float(input("What was the total bill? $"))

# Asking the user for the tip%
tip_percentage = int(input(
    "What percentage tip would you like to give? 10, 12, or 15 ? "))

# Asking for the number of people to split the bill between
number_of_people = int(input("How many people to split the bill? "))

# Calculating tip value:
tip_value = total_bill * tip_percentage / 100

# Calculating bill with tip:
bill_with_tip = tip_value + total_bill

# Calculating bill paid by each person
bill_paid_by_each = bill_with_tip / number_of_people

# Formatting the final amount to show 2 decimal places
bill_paid_by_each = "{:.2f}".format(bill_paid_by_each)

# Result
print(f"Each person should pay: ${bill_paid_by_each}")

# Feedback:
# 1. The solution works as intended, but the price should be printed up till 2 decimal places, Try using 150 for amount, 12 for tip and 5 people. The old solution (using round) would give 33.6, instead of 33.60.
# 2. So this is more of a formatting problem, than a mathematical rounding one. So we'll use try using formatting instead of using math, useing the format function.
