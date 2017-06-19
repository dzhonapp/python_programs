'''In mathematics, the notation n! represents the factorial of the nonnegative integer n . The
factorial of n is the product of all the nonnegative integers from 1 to n. For example,
7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040
and
4! = 1 x 2 x 3 x 4 = 24
Write a program that lets the user enter a nonnegative integer and then uses a loop to calculate
the factorial of that number. Display the factorial.'''

number=8

fact_result=1
for i in range(number):
    fact_result *= (i+1)

print(fact_result)