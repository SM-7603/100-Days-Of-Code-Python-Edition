# Description: Borrowing the code that I wrote for the roller coaster program, and then adding successive if-statements :D

# Declare variables
ticket_price_kid = 5
ticket_price_teen = 7
ticket_price_adult = 12

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
want_photo = (input("Do you want to take a picture? (y / n) "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        if want_photo == "y":
            print(f"Please pay ${ticket_price_kid + 3}")
        else:
            print(f"Please pay ${ticket_price_kid}")
    elif age <= 18:
        if want_photo == "y":
            print(f"Please pay ${ticket_price_teen + 3}")
        else:
            print(f"Please pay ${ticket_price_teen}")
    else:
        if want_photo == "y":
            print(f"Please pay ${ticket_price_adult + 3}")
        else:
            print(f"Please pay ${ticket_price_adult}")
else:
    print("Sorry, you have to grow taller before you can ride :D")
