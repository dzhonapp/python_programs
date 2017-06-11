'''4. Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message. The following
table shows the Roman numerals for the numbers 1 through 10:
'''

userInput = int(input('Please type the number you want to convert to Roman Numeral! '))
romanNumerals=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

while 0>userInput>10:
    userInput = int(input('Please type the number you want to convert to Roman Numeral! Between 0-10'))
else:
    print(romanNumerals[userInput - 1])
