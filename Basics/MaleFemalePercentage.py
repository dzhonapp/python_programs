'''
11. Male and Female Percentages
Write a program that asks the user for the number of males and the number of females registered
in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
class. The percentage of males can be calculated as 8 4 20 5 0.4, or 40%. The percentage
of females can be calculated as 12 4 20 5 0.6, or 60%.
'''

males=int(input('How many male students in the class? '))
females =int(input('How many female students in the class? '))
percentage = 100/(males+females)
print('Total male percentage is:', males*percentage, '%', 'female percentage is', females*percentage,'%', sep=' ')