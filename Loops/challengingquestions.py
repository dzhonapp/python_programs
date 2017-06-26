import copy

A=[[13,4,8,14,1],[9,6,3,7,21], [5,12,17,9,3],[5,12,17,9,3],[5,12,17,9,3]]

B=[]

for i in range(len(A[0])):
    B.append(list())
    for y in range(len(A)):
        B[i].append(A[y][i])


print(B)
