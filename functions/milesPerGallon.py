'''Miles-per-Gallon
A car’s miles-per-gallon (MPG) can be calculated with the following formula:
MPG = Miles driven / Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car’s MPG and display the result.
'''


def mpgCalculate():
    miles = float(input('How many miles you drove?'))
    gallons= float(input('How many gallons of gas you filled? '))
    return miles/gallons



print('Your MPG is: ', mpgCalculate())