# Rolling the dice
import random
#randint function example
def dice():
    again = 'y'.lower()
    while again=='y':
        print('Rolling the dice...')
        print ('Theri values are: ')
        print(random.randint(1, 6) )
        print(random.randint(1, 6) )

        again = input('Would you like to roll again? ')
    else:
        print("THank you for playing our game! ")

dice()