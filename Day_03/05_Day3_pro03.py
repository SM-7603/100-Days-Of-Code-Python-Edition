# Warning - This is a difficult challenge (could take anywhere from 10-40 mins)
# Tip: Try drawing out the flow chart and writing out the pseudoCode for this problem on a piece of paper, it would be good practice... :D 

# Leap year conditions: (For every year thats:)
# 1. Perfectly divisible by 4
#   -  Except when its perfectly divisible by 100
#       - Unless its perfectly divisible by 400

# PseudoCode:
# start
# input year
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             output "yes"
#         else:
#             output "no"
#     else:
#         output "yes"
# else:
#     output "no"

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year :D")
        else:
            print(f"{year} is not a leap year :(")
    else:
        print(f"{year} is a leap year :D")
else:
    print(f"{year} is not a leap year :(")