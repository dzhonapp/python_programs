'''13. Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.50
Over 2 pounds but not more than 6 pounds $3.00
Over 6 pounds but not more than 10 pounds $4.00
Over 10 pounds $4.75
Write a program that asks the user to enter the weight of a package and then displays the
shipping charges.'''

pack_weight = float(input('What is the weight of package? '))
rate=0
if 0<pack_weight<=2: rate+=1.5
elif 2<=pack_weight<6: rate+=3
elif 6<= pack_weight<10: rate+=4
elif pack_weight>=10: rate+=4.75
else: ('Wrong input! ')

total= rate*pack_weight
print('Your total is:', format(total, ',.2f'),'USD, rate applied per pound is $',rate, sep=' ')