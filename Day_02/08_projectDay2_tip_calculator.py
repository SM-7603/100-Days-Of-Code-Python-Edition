# Program Description: The program should ask the total bill, the percentage of tip to be given and the number of people to split the bill between. The final amount must be rounded off till 2 decimal places.

# Greeting message
print("Welcome to the tip calculator!")

# Asking the user for the total bill
total_bill = input("What was the total bill? $")

# Asking the user for the tip%
tip_percentage = input(
    "What percentage tip would you like to give? 10%, 12%, or 15% ? ")

# Calculating the value of tip:
tip_value = float(tip_percentage) * float(total_bill) / 100

# Asking for the number of people to split the bill between
number_of_people = input("How many people to split the bill? ")

# Calculating bill paid by each and rounding it off to 2 decimal places
bill_paid_by_each = round(
    (float(total_bill) + tip_value) / float(number_of_people), 2)

# Result
print(f"Each person should pay: ${bill_paid_by_each}")
