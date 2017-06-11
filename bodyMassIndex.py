from math import pow
'''14. Body Mass Index
Write a program that calculates and displays a person’s body mass index (BMI). The BMI
is often used to determine whether a person is overweight or underweight for his or her
height. A person’s BMI is calculated with the following formula:
BMI = weight x 703/height(square)
where weight is measured in pounds and height is measured in inches. The program
should ask the user to enter his or her weight and height and then display the user’s BMI.
The program should also display a message indicating whether the person has optimal
weight, is underweight, or is overweight. A person’s weight is considered to be optimal
if his or her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered
to be underweight. If the BMI value is greater than 25, the person is considered
to be overweight.'''
height = float(input('Please write your height!'))*12 #Multiplying to 12 is for that 1 feet is 12 inches so 5.6 as in DL * 12 will return total in inches
weight = float(input('Please write your weight!'))
condition=""
body_mass_index = (weight*703/pow(height, 2))
if 18.5<=body_mass_index<=25: condition+='Optimal'
elif body_mass_index<18.5: condition+='Underweight'
elif body_mass_index>25: condition+='Overweight'

print('You are in', condition, 'condition, your body mass index is:', format(body_mass_index, ',.2f'))
