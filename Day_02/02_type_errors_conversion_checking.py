# This down below, will give us a TypeError as seen in the previous file
# len(123)

num_char = len(input("What is your name? "))
# This will also give us a type error: "TypeError: can only concatenate str (not "int") to str"
# print("Your name has " + num_char + " characters.")

# How to see the datatypes that we are working with?
# Type Checking
# We can use the type() function or use intellisense to check the type of DataType that the variable is.
# print(type(num_char))
# print(type("num_char"))

# Type Conversion

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

# Mini Quiz (example): Guess what the answer will be?

# print(70 + float("100.5"))
# print(str(70) + str(100))