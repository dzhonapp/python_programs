'''8. Hot Dog Cookout Calculator
Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8.
Write a program that calculates the number of packages of hot dogs and the number of
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.
The program should ask the user for the number of people attending the cookout and the
number of hot dogs each person will be given. The program should display the following
details:
• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over'''

people= int(input('How many people will attend? '))
hotDogsGiven = int(input('How many hot dogs will be given to people? '))

requiredHotdogs = people*hotDogsGiven
print("Required hot dogs: ", requiredHotdogs)
print("Required bun packages: ", requiredHotdogs/8)
leftoverHotdog = 0 if requiredHotdogs%10==0 else requiredHotdogs%10
leftoverBuns = 0 if requiredHotdogs%8==0 else requiredHotdogs%8
print("Leftover hotdog: ", leftoverHotdog)
print('Leftover buns: ', leftoverBuns)
