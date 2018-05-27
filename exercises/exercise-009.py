# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

print('Please, write all you want. When you finish just leave a blank space before press enter')

lines = list()
raw = input()

while (raw.strip() != ''):
    lines.append(raw.upper())
    raw = input()

for line in lines:
    print(line)
