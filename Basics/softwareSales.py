'''A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:
Quantity Discount
10–19       10%
20–49       20%
50–99       30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.'''

package_bought= int(input('How many packages you would like to buy? '))
discount=0
package_price = 99
if 10<=package_bought<=19: discount+=10
elif 20<=package_bought<=49: discount+=20
elif 50<=package_bought<=99: discount+=30
elif package_bought>=100: discount =+40
else: print('Wrong entry! ')

print("Total sum is:", package_bought*package_price, "$,", discount,'% discount apply,',\
      'last price is', format(package_price*package_price*(discount/100), ',.2f'), '$', sep=' ')
