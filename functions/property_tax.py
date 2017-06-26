'''
A county collects property taxes on the assessment value of property, which is 60 percent
of the property’s actual value. For example, if an acre of land is valued at $10,000, its
assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment
value. The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for
the actual value of a piece of property and displays the assessment value and property tax.
'''

value_property=float(input("What is the actual value of your property? "))
def assesmentValue_propeTax(valueofProperty):
    '''
    Calculates the assesment value of property and its tax, 72 cents per100$ of the assesment value, assesment value is 60% of actual value
    :return: Prints out the results:
    '''
    assesment = value_property*0.6
    tax = format(assesment/10000*72, ',.2f') # This result cents
    print("The assesment price of your property is: $")
    print(assesment)
    print('The tax of your property is: $')
    print(tax)


assesmentValue_propeTax(value_property)