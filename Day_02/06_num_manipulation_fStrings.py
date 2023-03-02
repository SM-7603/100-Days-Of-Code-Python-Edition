# Let's take an example
print(8 / 3)
# Notice how the single division still gives us a float as an output: (This doesn't happen with floor division "//", instead we get an int.)
print(type(8 / 2))

# Removing everything after the decimal. (kind of like floor rounding)
print(int(8 / 3))

# Simply using the round() function
print(round(8 / 3))

# Rounding floats by specifying the number of decimals
print(round(8 / 3, 2))
print(round(2.6666666666666666, 2))

# Floor division using "//" (converts to an int)
print(8 // 3)
print(type(8 // 3))

# Using variables to store the calculations and using shorthand calculations
# example 1
result = 4 / 2
result /= 2
print(result)

# example 2
score = 0
height = 1.8
isWinning = True
# score = score + 1 
# We prefer the shorthand below, it's very useful as we often have to manipulate a value based on its previous value in programming.
score += 1

print(score)

# Note: For the shorthand we could also do: -=, +=, /=, *=, %=

# f-Strings: it's great as it saves us from a lot of pain of making sure that all the dataTypes are same
# print("Your score is " + str(score) + ", your height is " + str(height) + ", and you are winning is " + str(isWinning))
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}")