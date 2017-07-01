'''
11. Math Quiz
Write a program that gives simple math quizzes. The program should display two random
numbers that are to be added, such as:
247
+ 129
The program should allow the student to enter the answer. If the answer is correct, a message
of congratulations should be displayed. If the answer is incorrect, a message showing
the correct answer should be displayed.
'''

import random

print('Here your math quiz startes!')

quittingQuiz = True
while quittingQuiz:
    a = random.randint(1, 100)
    b = random.randint(0, 100)
    result = a + b
    print("Please write the answer ", a, "+", b, "('To exit -> 0')")
    userAnswer = int(input(''))
    if userAnswer == result:
        print('Congrats you won! ')
    elif userAnswer == 0:
        quittingQuiz = False
        print('Come back again! ')
    else:
        print('Wrong answer! ')

