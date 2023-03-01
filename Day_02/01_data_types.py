# This creates a type error: "TypeError: object of type 'int' has no len()"

# remember that len() gives an int as the output
# print(len(123))

# Data Types
# 1. String
# Subscript (Process = subscripting)
# "Hello"[n], where n (the index) = any integer from 0 to len(Hello) - 1" (as even though there are 5 lettters, the last digit will have an index of "4") (Always remember computers always count from 0's.)

# Printing the 1st character of the string - "Hello"
print("The 1st character of the word Hello is " + "Hello"[0])

# Printing the last character of the string - "Hello"
print("The last character of the word Hello is " + "Hello"[4])
# print("The last character of the word Hello is " + "Hello"[len("Hello") - 1]) # This will work for any variable

# Adding strings (concatenating) {Remember its still text}

# This doesn't add up, like you would expect huh? lol
print("123" + "345")

# Integer

# This works like you would normally expect.
print(123 + 345)

# Commonly a number like 123456789 would be represented like this => 123,456,789 or 12,34,56,789 by using "," to seperate the number and make it easier to read for us humans. (But computers don't need that, and you can't add commas to your numbers in your code.) 
print(123456789)
# Instead you could do this: (Adding "_" to your numbers can be used to make it easier for us "humans" to read the numbers, but python ignores the _'s and runs the code like usual.)
print(123_456_789) 

# Float (the decimal point can float around the number, hence the name)

3.14159

# Boolean

True
False

# Quiz:

# This is still a float, the "_" is just for readability purpose.
print(123_456.9)