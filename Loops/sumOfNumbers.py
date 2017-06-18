'''8. Sum of Numbers
Write a program with a loop that asks the user to enter a series of positive numbers. The
user should enter a negative number to signal the end of the series. After all the positive
numbers have been entered, the program should display their sum.'''
flag=True
total=0
while flag:
    ask=float(input('Type positive numbers to continue, negative to exit!'))
    if ask>0:
        total+=ask
    elif ask<0:
        flag=False
print(total)