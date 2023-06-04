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

# Rounding the calculation:
bill_paid_by_each = round(bill_paid_by_each, 2)

# Formatting the final amount to show 2 decimal places
bill_paid_by_each = "{:.2f}".format(bill_paid_by_each)

# Result
print(f"Each person should pay: ${bill_paid_by_each}")

# Feedback:
# 1. The solution works as intended, but the price should be printed up till 2 decimal places, Try using 150 for amount, 12 for tip and 5 people. The old solution (using round) would give 33.6, instead of 33.60.
# 2. So this is more of a formatting problem, than a mathematical rounding one. So we'll use try using formatting instead of using math, using the format function.

# Update:
# Turns out there's no substitute for math :P
# All the string formatting is doing is... well string formatting, i.e. It isn't really rounding anything, its just getting rid of the decimal points after the 2nd decimal place & placing a "0" in the 2nd place if there's no 2nd decimal place.
# Meaning, there's still a need to round the final answer as we need an accurate answer (which we get by using rounding) & then displaying the final answer by using string formatting ("{:.2f}"".format(whatEver)) :D