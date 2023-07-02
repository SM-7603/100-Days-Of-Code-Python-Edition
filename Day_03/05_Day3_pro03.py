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

# A "small" observation I made:
# 1. I found that breaking down the leap year conditions into multiple if statements and focusing on the immediate condition helped in understanding the logic more clearly. 
# 2. By first handling the else block and then moving on to the nested if statements, I could avoid getting overwhelmed by nested conditions and potential confusion.
# 3. This problem-solving technique allowed me think clearly & not get lost. 
# 4. It redirected my focus to what was right in front of me and prevented me from falling into a rabbit hole of nested conditions. 
# 5. Additionally, drawing the flowchart and writing the pseudoCode beforehand proved to be helpful for understanding the problem and guiding the implementation. 
# 6. Also, I feel I could now rely on this technique and just jump straight to write the pseudoCode without the flowchart :D
