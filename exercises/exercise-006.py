# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
import math

def formula(d):
    if isinstance(d, str): d = int(d)
    c = 50
    h = 30
    x = (2 * c * d) / h
    return int(math.sqrt(x))

raw = input('Please give me numbers (sepparated by comma): ')

strings = raw.split(',')

numbers = list(map(formula, strings))

print(numbers)
