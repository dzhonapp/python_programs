
print("Please write the file name you want to view!")
fileName = input()
file = open(fileName, "r")

content = file.read().split("\n")

for i in range(5):
    print("Line Number: ", i+1, " is : ", int(content[i]))


#for i in content:
 #   i = int(i)
# Counts the Items in the File
content.remove("")
for i in range (len(content)):
    content[i] = int(content[i])
# average of the numbers in the file
print(sum(content)/len(content))

