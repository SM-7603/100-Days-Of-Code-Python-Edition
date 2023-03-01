# Swap the values of a and b, without assigning a = 20 & b = 10. ("That's cheating, that's wrong)
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

print("The value of a = " + str(a))
print("The value of b = " + str(b))

# Solution
c = a
a = b
b = c

print("The value of a = " + str(a))
print("The value of b = " + str(b))