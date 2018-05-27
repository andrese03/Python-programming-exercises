# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class MyClass:

    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input('Please give me a string: ')

    def pringString(self):
        print(self.s.upper())

myClass = MyClass()
myClass.getString()
myClass.pringString()