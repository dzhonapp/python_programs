'''Create a change-counting game that gets the user to enter the number of coins required
to make exactly one dollar. The program should prompt the user to enter the number of
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
dollar, the program should congratulate the user for winning the game. Otherwise, the
program should display a message indicating whether the amount entered was more than
or less than one dollar.'''

pennies = int(input('Enter pennies amount!'))*1
nickels = int(input('Enter nickels amount!'))*5
dimes = int(input('Enter dimes amount!'))*10
quarters = int(input('Enter quartes amount!'))*25
total = pennies+nickels+dimes+quarters
if total==100:
    print('Congratualtions preciesly oNe dollar')
elif total>=100:
    print(('You entered more than one dollar'), total)
else:
    print("You entered less than one dollar", total)
