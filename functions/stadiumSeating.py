'''
7. S tadium Seating
There are three seating categories at a stadium. For a softball game, Class A seats cost $20,
Class B seats cost $15, and Class C seats cost $10. Write a program that asks how many
tickets for each class of seats were sold, and then displays the amount of income generated
from ticket sales.
'''

sold_A_ticket= int(input('How many "A" class ticket was sold? '))
sold_B_ticket= int(input('How many "B" class ticket was sold? '))
sold_C_ticket= int(input('How many "C" class ticket was sold? '))


def calculateSales(aAmount, bAmount, cAmount):
    aClassSeat= 20
    bClassSeat = 15
    cClassSeat = 10
    print("A class ticket total sold ", sold_A_ticket, ' pcs. And total earning is : ', sold_A_ticket * aClassSeat)
    print("B class ticket total sold ", sold_B_ticket, ' pcs. And total earning is : ', sold_B_ticket * bClassSeat)
    print("C class ticket total sold ", sold_C_ticket, ' pcs. And total earning is : ', sold_C_ticket * cClassSeat)
    print('Overall total tickets sold: ', sold_A_ticket+sold_B_ticket+sold_C_ticket, ' pcs. And total earning is: ', sold_A_ticket * aClassSeat+sold_B_ticket*bClassSeat+sold_C_ticket*cClassSeat)

calculateSales(sold_A_ticket, sold_B_ticket, sold_C_ticket)
