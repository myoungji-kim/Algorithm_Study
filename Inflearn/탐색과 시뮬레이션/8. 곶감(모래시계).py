from sys import stdin
from collections import deque


# 1 - My Code
N = int(stdin.readline())
graph = [deque(map(int, stdin.readline().split())) for _ in range(N)]
lt, rt = 0, N
M = int(stdin.readline())
rotate = [list(map(int, stdin.readline().split())) for _ in range(M)]
res = 0

# 회전
for i in range(M):
    for _ in range(rotate[i][2]):
        if rotate[i][1] == 0:
            graph[rotate[i][0] - 1].append(graph[rotate[i][0] - 1].popleft())
        else:
            graph[rotate[i][0] - 1].appendleft(graph[rotate[i][0] - 1].pop())

# 합 구하기
for i in range(N):
    for j in range(lt, rt):
        res += graph[i][j]

    if i < N // 2:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt += 1

print(res)


