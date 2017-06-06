def printingOdds(myList):
    return [x for x in myList if x%2 != 0]
myList=[1, 3,2,4,4,5,6, 5,55,4, 33,44,66,77,88,44,33,22,11,33]
print(printingOdds(myList))