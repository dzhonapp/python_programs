'''Write a program that uses nested loops to collect data and calculate the average rainfall
over a period of years. The program should first ask for the number of years. The outer loop
will iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.'''

yearsToCalculate = int(input('How many years would you like to calculate rainfall? '))
monthlyRainfall = 0.0
for i in range(yearsToCalculate):
    for month in range(1, 13):
        print('Month #', month, end=" ")
        monthlyRainfall += float(input('Please input the rainfall! '))

    print('For year ', i+1, 'the total rainfall was: ', monthlyRainfall, 'inches')

print('The average rainfall was: ', format(monthlyRainfall/(yearsToCalculate*12, ',.2f')))


