'''2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.'''
burnedCalories=0
for burnedCal in range(0, 31, 5):
    burnedCalories+=4.2*burnedCal
print(burnedCalories)