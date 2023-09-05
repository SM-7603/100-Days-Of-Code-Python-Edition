# Task: We're building a pizza order program here

# Based on the user's input, we need to work out the customer's final bill

""" 
Meta Data:

- Pizza Prices: 
    - S = $15
    - M = $20
    - L = $25

- Pepperoni:
    -  S  = +$2
    - M/L = +$3

- Extra Cheese:
    - Any size = +$1

"""

# Here's the starter code:

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# write you code below 👇👇👇

# attempt 1 (obviously unoptimized)

# create the if-else condition

# variable for bill

bill = 0 # setting a default value

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

# store the formatted output as an fString

output_message = f"Your final bill is: ${round(bill, 2)}."

# print the output

print("========================")

print(output_message)

print("========================")
