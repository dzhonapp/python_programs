import random
# random.random() function return floationg point number, takes no arguments showing from 0, 1.0 (one is excluded!).
print(random.random())


# random.uniform() allows you to show the range, and also returns the floating point number!
print(random.uniform(1, 9.74))

# random.seed() to get same random numbers each time
#EXAMPLE:

random.seed(10)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))