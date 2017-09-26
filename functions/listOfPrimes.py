'''
18. P rime Number List
This exercise assumes that you have already written the is_prime function in Programming
Exercise 17. Write another program that displays all of the prime numbers from 1 to 100.
The program should have a loop that calls the is_prime function.
'''

def isPrime(n): # Function returns True or False, if Prime or not!
    n = abs(int(n))
    if n < 2:
        return False
    elif not n & 1:
        return False
    elif n == 2:
        return True
    for y in range(3, int(n**0.5)+1, 2):
        if n % y == 0:
            return False
    return True


def primes(final): # Creates the list of numbers 0, to final if it is prime!
    listOP = []
    for i in range(final):
        if isPrime(i):
            listOP.append(i)
    return listOP


