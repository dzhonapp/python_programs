'''
Day of the Week
Write a program that asks the user for a number in the range of 1 through 7. The program
should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
display an error message if the user enters a number that is outside the range of 1 through 7.

'''

user_input = int(input("What is the day of the week? "))

daysOfWeek = {1: "Monday", 2: "Tuesday", 3: "Wednsday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

if 0<user_input<7:
    print("Today is : " + daysOfWeek[user_input])
else:
    print("Are you sure? ")