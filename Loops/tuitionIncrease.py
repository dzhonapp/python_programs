'''
10. T uition Increase
At one college, the tuition for a full-time student is $8,000 per semester. It has been
announced that the tuition will increase by 3 percent each year for the next 5 years. Write
a program with a loop that displays the projected semester tuition amount for the next 5
years.
'''
tuition =8000;
year=5
print('First year tution: ', tuition)
for i in range(year):
    tuition +=tuition*0.03
    print("Next year tutition:", format(tuition, ",.2f"))

