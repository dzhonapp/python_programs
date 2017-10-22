import os

a = os.listdir("/Users/bma/Documents/Python_programs/python_programs/Files")
file = open("emplyee.txt", "r")
fileread = file.readlines()
def newFile():
    newFile = []
    for word in fileread:
        newFile.append(word.rstrip("\n"))
    return newFile

print(newFile())
print(a)