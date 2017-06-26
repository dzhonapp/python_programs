'''
3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a program
that asks the user to enter the replacement cost of a building and then displays the
minimum amount of insurance he or she should buy for the property.
'''

def insurance_house():
    replacement_cost = float(input('What is the minimum cost of building? '))
    return replacement_cost*0.8

print(insurance_house(), " $ is minimum amount of insurance you should buy for your property to cover everything! ")

