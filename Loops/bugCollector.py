'''
1. Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.
'''

days=int(input("How many days? "))

numberOfBugs=int(input('How many bugs are collected per day! '))

total_bugs=0;

for day in range(days):
    total_bugs+=numberOfBugs

print(total_bugs)