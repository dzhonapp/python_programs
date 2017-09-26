import random

toss = 10
HEADS = 1
TAILS = 0

for i in range(toss):
    if random.randint(TAILS, HEADS) == HEADS:
        print("Heads")
    else:
        print("Tails")

def fuc(n):
    print( n%9 or n and 9)

# Printing example 908 9+0+8 = 17
# 1+7 = 8
# Unless there is only one digit!
