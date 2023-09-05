# Description: Borrowing the code that I wrote for the roller coaster program, and then adding successive if-statements :D & then further adding logical operators

# Task: 
# Use logical operators to make tickets free for people going through their mid-life crisis
# Ages b/w [45 - 55]

# Declare variables
bill = 0

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Please pay ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Please pay ${bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Rest assured, everything will turn out fine, enjoy a free ride!!! :D")
    else:
        bill = 12
        print(f"Please pay ${bill}")
    
    want_photo = (input("Do you want to take a picture? (y / n) "))
    if want_photo == "y":
        bill += 3 # as the bill increments by $3 for the ticket
    
    print(f"Please pay ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride :D")
