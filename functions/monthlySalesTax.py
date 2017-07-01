'''
9. Monthly Sales Tax
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter the
total sales for the month. From this figure, the application should calculate and display the
following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
'''

stateSaleTax = 0.05
countySaleTax = 0.025
totalSalesMonth = float(input('What is total sales for the month? '))
print("County Sales tax: $", totalSalesMonth*countySaleTax)
print("State sales tax: $", totalSalesMonth*stateSaleTax)
print('Total tax amount', totalSalesMonth*countySaleTax+totalSalesMonth*stateSaleTax)
