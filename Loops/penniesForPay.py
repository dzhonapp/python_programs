'''
Write a program that calculates the amount of money a person would earn over a period
of time if his or her salary is one penny the first day, two pennies the second day, and
continues to double each day. The program should ask the user for the number of days.
Display a table showing what the salary was for each day, and then show the total pay at
the end of the period. The output should be displayed in a dollar amount, not the number
of pennies.
'''

days= int(input('Please type the work day! '))
totalPay=1;
for day in range(1,days):
    print(totalPay)
    totalPay*=2
