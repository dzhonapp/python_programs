'''3. Budget Analysis
Write a program that asks the user to enter the amount that he or she has budgeted for
a month. A loop should then prompt the user to enter each of his or her expenses for the
month and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget.'''

amountBudgeted=float(input('What is the amount you budgeted for a month? '))
tempAmountBudgeted=amountBudgeted
flag = 0
while flag<5:
    expense = float(input('Write you expenses! '))
    amountBudgeted-=expense
    print(amountBudgeted)
    flag+=1
print('Your budget was: ', tempAmountBudgeted)
if amountBudgeted<0:
    print("You spend more than your budget for: ", "-",(tempAmountBudgeted-amountBudgeted)-amountBudgeted)
else:
    print('You spend less than your budget and saved: ', amountBudgeted)


