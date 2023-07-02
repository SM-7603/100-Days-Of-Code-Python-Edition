# Description: Borrowing the code that I wrote for the roller coaster program, and then adding successive if-statements :D

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
    else:
        bill = 12
        print(f"Please pay ${bill}")
    
    want_photo = (input("Do you want to take a picture? (y / n) "))
    if want_photo == "y":
        bill += 3 # as the bill increments by $3 for the ticket
    
    print(f"Please pay ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride :D")
