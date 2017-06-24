'''Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise you
were asked to write a program that calculates and displays the county and state sales tax
on a purchase. If you have already written that program, redesign it so the subtasks are in
functions. If you have not already written that program, write it using functions.

Exercise #6: 6. S ales Tax
Write a program that will ask the user to enter the amount of a purchase. The program
should then compute the state and county sales tax. Assume the state sales tax is 5 percent
and the county sales tax is 2.5 percent. The program should display the amount of the purchase,
the state sales tax, the county sales tax, the total sales tax, and the total of the sale
(which is the sum of the amount of purchase plus the total sales tax).
Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
'''

def ask():
    answer= float(input('Please write down the amount of purchase'))
    return answer


def tax():
    stateSalesTax = 0.05
    countySalesTax = 0.025
    purchase = ask()
    totalTax = (purchase*stateSalesTax)+(countySalesTax*purchase)
    print('Total Tax : ', format(totalTax, ',.2f'))
    print('State Tax : ', format(purchase*stateSalesTax, ',.2f'))
    print('Sales Tax : ', format(purchase*countySalesTax, ',.2f'))
    print(' : ', format(purchase-totalTax, ',.2f'))


tax()