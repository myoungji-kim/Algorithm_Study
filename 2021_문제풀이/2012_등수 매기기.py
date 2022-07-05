from collections import deque
from sys import stdin

N = int(stdin.readline())
A = [int(stdin.readline()) for i in range(N)]
B = deque([i + 1 for i in range(N)])

A = deque(sorted(A))
angry = 0
temp = []

for i in range(N):
    if A[0] == B[0]:
        A.popleft()
        B.popleft()
    else:
        temp.append(A.popleft())

for i in range(len(temp)):
    angry += abs(temp[i] - B[i])

print(angry)
