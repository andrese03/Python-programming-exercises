# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

amount = 0
while True:
	raw = input("Make a transaction: ")
	if not raw:
		break
	args = raw.split(' ')
	operation = args[0]
	value = float(args[1])
	if operation is 'D':
		amount += value
	elif operation is 'W':
		amount -= value
	else:
		pass

print('Total amount:', amount)
