# Description: Data Type 1st Exercise problem for Day 2 
# Ask the user for a two digit number and add the digits up as the final output.

two_digit_number = input("Type a two digit number: ")

# M.1 (Short and sweet)
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# M.2 (Looks better and is easier to understand)
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)

# Concepts used: 
# 1. SubScripting
# 2. TypeConversion
# 3. TypeChecking (didn't use it here, but I knew that the input always gave us a string, type() is what you would use to figure that fact out.)