'''1. Day of the Week
Write a program that asks the user for a number in the range of 1 through 7. The program
should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
display an error message if the user enters a number that is outside the range of 1 through 7.'''

day = int(input('What day?'))

while day<1 or day>7:
    day = int(input('What day? between 1-7'))
if day == 1:
    print("Monday")
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednsday')
elif day ==4:
    print("Thursday")
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
else:
    print('Sunday')
