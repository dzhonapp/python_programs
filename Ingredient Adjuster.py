'''

10. I ngredient Adjuster
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, and then displays the number of
cups of each ingredient needed for the specified number of cookies.
'''

#oneCookie = 1.5/48, 1/ 48, 2.75/48
sugarForOne = 1.5/48
butterForOne= 1/48
flourForOne=2.75/48

askForCookieQuantity = int(input('How many cookies you want to cook? '))
print('You will need Sugar:', askForCookieQuantity * sugarForOne, 'Butter:', askForCookieQuantity * butterForOne, 'Flour:', askForCookieQuantity * flourForOne, 'cups', sep=' ')

