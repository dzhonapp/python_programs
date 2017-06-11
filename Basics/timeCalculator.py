'''15. Time Calculator
Write a program that asks the user to enter a number of seconds and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should display the number of minutes in that many
seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should display the number of hours in that
many seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is
greater than or equal to 86,400, the program should display the number of days in that
many seconds.'''

seconds = int(input('Input the seconds! '))

minutes = 0
day=0
hours= 0

if seconds<3600:
    minutes=seconds//60
    seconds=seconds-(minutes*60)
    print(minutes)
elif seconds>=3600:
    hours = seconds // 3600
    minutes = seconds-(hours*3600)//60
    seconds=seconds-((hours*3600)+(minutes*60))
elif seconds>=86400:
    day = seconds // 86400
    hours = seconds - (day * 86400) // 3600
    minutes = seconds - ((day * 86400) + (hours * 3600)) // 60
    seconds = seconds - ((day * 86400) + (hours * 3600) + (minutes * 60))

print('You have entered: ', seconds, 'seconds', sep=' ')
print(day, ": Day(s), ", hours, ": Hour(s), ", minutes, ": Minute(s), ", seconds, ' :Seconds,')
