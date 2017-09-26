'''19. Future Value
Suppose you have a certain amount of money in a savings account that earns compound
monthly interest, and you want to calculate the amount that you will have after a specific
number of months. The formula is as follows:
F = P x (1 + i)power(t)
The terms in the formula are:
• F is the future value of the account after the specified time period.
• P is the present value of the account.
• i is the monthly interest rate.
• t is the number of months.
Write a program that prompts the user to enter the account’s present value, monthly interest
rate, and the number of months that the money will be left in the account. The program
should pass these values to a function that returns the future value of the account, after the
specified number of months. The program should display the account’s future value.
'''

presentValue = float(input("Please enter amount you have in the bank! "))
interestRate = float(input("Please enter the interest rate 0-100!"))/100
duration = int(input("Please type how long your money going to be in the bank? "))

def futureValueCalculator(money, inRate, time):
    return money*(pow((1+inRate), time))
print(round(futureValueCalculator(presentValue, interestRate, duration), 2))
