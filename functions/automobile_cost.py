'''Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
'''
def monthly_cost_auto():
    expense_loan = float(input('What amount of loan you are paying monthly for your vehicle? '))
    expense_insurance = float(input("What is your monthly insurance? "))
    expense_gas = float(input('What is your gas expense (monthly)? '))
    expense_oil=float(input('What is your oil change expense monthly? '))
    expense_tires = float(input('What is your expense for tires per month? '))
    expense_maint= float(input('What is your expense for maintenance of your vehicle? '))
    print('Your total expense per month is: ', expense_gas + expense_insurance + expense_loan + expense_maint + expense_oil + expense_tires)
    print('Your annual total expense: ', (expense_gas + expense_insurance + expense_loan + expense_maint + expense_oil + expense_tires)*12)

monthly_cost_auto()