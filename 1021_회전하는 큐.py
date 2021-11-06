from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())
outList = deque(list(map(int, stdin.readline().split())))
numList = deque([i + 1 for i in range(N)])
answer = 0

while len(outList) != 0:
    if outList[0] != numList[0]:
        if numList.index(outList[0]) <= len(numList) // 2:
            while outList[0] != numList[0]:
                numList.append(numList.popleft())
                answer += 1
        else:
            while outList[0] != numList[0]:
                numList.appendleft(numList.pop())
                answer += 1
    outList.popleft()
    numList.popleft()

print(answer)
