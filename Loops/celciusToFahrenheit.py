'''
6. Celsius to Fahrenheit Table
Write a program that displays a table of the Celsius temperatures 0 through 20 and
their Fahrenheit equivalents. The formula for converting a temperature from Celsius to
Fahrenheit is
F =  9/5C + 32
where F is the Fahrenheit temperature and C is the Celsius temperature. Your program must
use a loop to display the table.
'''
print('Fahranheit:\t\t\tCelcius:')
for celcius in range(21):
    print(" ",format((9/5*celcius +32), ',.2f'), "\t\t\t", celcius)
