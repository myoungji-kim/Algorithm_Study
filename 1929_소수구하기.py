import math
from sys import stdin

M, N = map(int,stdin.readline().split())

array = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

for i in range(M, N+1): #N부터
    if array[i] == True and i != 1:
        print(i)