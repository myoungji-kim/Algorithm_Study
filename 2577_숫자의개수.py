from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())

result = str(A*B*C)
cntNum = [0]*10

for i in range(len(result)):
    cntNum[int(result[i])] += 1

for i in range(len(cntNum)):
    print(cntNum[i])
