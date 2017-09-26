
def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    elif not n & 1:
        return False
    elif n == 2:
        return True
    for y in range(3, int(n**0.5)+1, 2):
        print(y)
        if n % y == 0:
            return False
    return True


