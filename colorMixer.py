'''
7. Color Mixer:
The colors red, blue, and yellow are known as the primary colors because they cannot
be made by mixing other colors. When you mix two primary colors, you get a secondary
color, as shown here:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.

Design a program that prompts the user to enter the names of two primary colors to mix. If
the user enters anything other than “red,” “blue,” or “yellow,” the program should display
an error message. Otherwise, the program should display the name of the secondary color
that results.
'''
print('What colors do you want to mix? ')
colorMixUser_1= input('Pick first Color ').upper()
colorMixUser_2=input('Pick second Color ').upper()
if colorMixUser_1=='RED' and colorMixUser_2 == "BLUE":
    print("Purple")
elif colorMixUser_1=="RED" and colorMixUser_2=="YELLOW":
    print('Orange')
elif colorMixUser_2=="YELLOW" and colorMixUser_1== "BLUE":
    print('Green')
else:
    print('You chose something different! ')