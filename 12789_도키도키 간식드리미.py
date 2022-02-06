from sys import stdin
from collections import deque

n = int(stdin.readline())
row = deque(list(map(int, stdin.readline().split())))
wait = []
getSnack = 0

while len(row) != 0:
    if getSnack + 1 == row[0]:
        getSnack = row.popleft()
    elif len(wait) != 0 and getSnack + 1 == wait[-1]:
        getSnack = wait.pop()
    else:
        wait.append(row.popleft())

while len(wait) != 0:
    if getSnack + 1 == wait[-1]:
        getSnack = wait.pop()
    else:
        print("Sad")
        exit()

print("Nice")