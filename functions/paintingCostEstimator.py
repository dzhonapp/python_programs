'''
8. P aint Job Estimator
A painting company has determined that for every 112 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $35.00 per
hour for labor. Write a program that asks the user to enter the square feet of wall space to
be painted and the price of the paint per gallon. The program should display the following
data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
'''

sq_feet_wall = float(input('What is the area of your wall in sq.ft? '))
paint_price_per_gallon = float(input('What is the price of paint per gallon? '))

def paint_job_estimate(area, price):
    gallon=area/112
    labor_cost=(gallon*8)*35
    gradn_total = gallon*price+labor_cost
    print("Total required gallons of paint is: $", format(gallon, '.2f'))
    print("Total required hours to finish job is: $", format(gallon*8, '.2f'))
    print("Total cost of paint is: $", format(gallon*price, '.2f'))
    print("Total cost for labor is: $", labor_cost)
    print("Total cost of painting is: $", format(gradn_total, '.2f'))

paint_job_estimate(sq_feet_wall, paint_price_per_gallon)


