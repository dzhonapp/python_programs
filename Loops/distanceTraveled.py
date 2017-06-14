'''
4. Distance Traveled
The distance a vehicle travels can be calculated as follows:
distance =  speed x time
For example, if a train travels 40 miles per hour for three hours, the distance traveled is
120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
and the number of hours it has traveled. It should then use a loop to display the distance
the vehicle has traveled for each hour of that time period. Here is an example of the desired
output:
What is the speed of the vehicle in mph? 40 (enter)
How many hours has it traveled? 3 (enter)
Hour    Distance Traveled
1           40
2           80
3           120
'''

speed= float(input("What is the speed of vechicle in km? "))
hours_elapsed=float(input('How much hours it traveled? '))
distance = 0
for i in range(int(hours_elapsed)):
    distance=distance+speed
    print("Traveled: \t", distance, "--","km")