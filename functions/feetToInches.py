'''
10. Feet to Inches
One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
of feet as an argument and returns the number of inches in that many feet. Use the function
in a program that prompts the user to enter a number of feet and then displays the number
of inches in that many feet.
'''

def feetToInches(feet):
    return feet*12
convert = int(input('Feet you want to convert to inches? '))

print('You have entered: ', convert, 'feet', sep=', ')
print(convert, " feets in inches is ", feetToInches(convert))