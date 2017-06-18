'''
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
application that displays the number of millimeters that the ocean will have risen each year
for the next 25 years.
'''
millimeters=1.6
for years in range(25):
    print("Year #", years+1)
    print('Millimeters risen so far: ', format(millimeters, ',.2f'))
    millimeters+=1.6

    