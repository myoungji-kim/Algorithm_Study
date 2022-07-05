from collections import deque
from sys import stdin

X = int(stdin.readline())
q = deque()
q.append([X])
answer = []

while q:
    a = q.popleft()
    n = a[0]
    if n == 1:
        answer = a
        break

    if n % 3 == 0:
        q.append([n // 3] + a)

    if n % 2 == 0:
        q.append([n // 2] + a)

    q.append([n - 1] + a)

print(len(answer) - 1)
print(*answer[::-1])
