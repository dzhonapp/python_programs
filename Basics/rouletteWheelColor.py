'''9. Roulette Wheel Colors
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
as follows:
• Pocket 0 is green.
• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
• For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the
pocket is green, red, or black. The program should display an error message if the user
enters a number that is outside the range of 0 through 36'''

user_choice= int(input('Type the roulette wheel color number! '))
if user_choice==0:
    print('Green')
elif 1<=user_choice<=10:
    if user_choice%2==0:
        print('Black')
    else:
        print('Red')
elif 11<=user_choice<=18:
    if user_choice%2==0:
        print('RED')
    else:
        print('BLACK')
elif 19<=user_choice<=28:
    if user_choice%2==0:
        print('Black')
    else:
        print('Red')
elif 29<=user_choice<=36:
    if user_choice%2==0:
        print('Red')
    else:
        print('Black')
elif user_choice not in range(36):
    print('Error, Out of range!')