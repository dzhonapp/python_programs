'''
12. Maximum of Two Values
Write a function named max that accepts two integer values as arguments and returns the
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
the function, the function should return 12. Use the function in a program that prompts the
user to enter two integer values. The program should display the value that is the greater
of the two.
'''
def max (a, b):
    if a > b:
        return a
    return b

print('Please type two integers! ')
a = int(input('Write any number! '))
b = int(input('Write any second value! '))

print('The greates number you entered is: ', max(a,b))
