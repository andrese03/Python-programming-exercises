# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def trim(x):
    return x.strip()

raw = input('Please provide me words: ')

strings = list(map(trim, raw.split(',')))

strings.sort()

print(strings)