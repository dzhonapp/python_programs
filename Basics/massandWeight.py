'''Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
the amount of mass of an object in kilograms, you can calculate its weight in newtons with
the following formula:
weight = mass x 9.8
Write a program that asks the user to enter an object’s mass, and then calculates its weight.
If the object weighs more than 500 newtons, display a message indicating that it is too
heavy. If the object weighs less than 100 newtons, display a message indicating that it is
too light.'''
mass = float(input('Please write the mass of an object in newtons! '))
if 100<mass<500:
    print(format(mass*9.8, ',.2f'))
elif mass<100:
    print('The weight is too light! ')
else:
    print('The weight is too heavy! ')
