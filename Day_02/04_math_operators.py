# Operators
4 + 8
7 - 7
3 * 2
6 / 3
2 ** 3

# Priority level
# PEMDAS/BEDMAS (from left to right) PEMDASLR/BEDMASLR
# ()
# **
# * /
# + -

# Question: What will the answer to this be?
3 * 3 + 3 / 3 - 3
# Ans = 7? (expectation)
# as 3 * 3 = 9 then 3 / 3 = 1
# => 9 + 1 - 3 = 7

# check, yes correct! its 7 :D
print(3 * 3 + 3 / 3 - 3)

# Now, after rearranging the operators the answer = 3.
# M.1: (Rearranging the higher priority operators around)
print(3 * 3 / 3 - 3 + 3)
# M.2: (Making lower priority operations to higher priority one's)
# Here we used the "()" to make the addition into the highest priority operation by surrounding it.
print(3 * (3 + 3) / 3 - 3)

# Notes (observations):
print(5 / 1)
# 1. Division always converts the DataType to float.
print(3 ** 2)
# 2. Python has an inbuilt exponent operator.