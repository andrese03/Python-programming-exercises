# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

raw = input("Write something:")

stats = { 'upper': 0, 'lower': 0 }

for char in raw:
	if char.isupper():
		stats['upper'] += 1
	elif char.islower():
		stats['lower'] += 1
	else:
		pass

print('UPPER: ', stats['upper'])
print('LOWER: ', stats['lower'])

