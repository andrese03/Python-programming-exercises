# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

raw = input('Write something: ')
stats = { 'digits': 0, 'letters': 0 }

for char in raw:
		if char.isdigit():
				stats['digits']+=1
		elif char.isalpha():
				stats['letters']+=1
		else:
				pass

print("LETTERS:", stats['letters'])
print("NUMBERS:", stats['digits'])

