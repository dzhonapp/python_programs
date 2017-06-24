'''8. T ip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, and then calculate the amount
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
'''
def restaurantTotal():
    total_meal= float(input('What is total cost of the meal? '))
    tip= total_meal*0.18
    tax = total_meal*0.07
    print('Total Meal cost: ', total_meal, '$')
    print('Total tip : $', format(tip, '.2f'), "\n",
          'Total tax: $ ', tax, "\n",
          'Grand total: $', format(total_meal+tip+tax, ',.2f'))

restaurantTotal()