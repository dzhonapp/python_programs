import random
'''Random from range function test, see how it behaves! '''
x =[x for x in range(10)]
print(x)
for i in range(10):
    print(x[random.randrange(1, 10)])
    print(x[random.randint(1, 9)], ' randint')

