from sys import stdin
from collections import deque


def bfs(X):
    cnt = 1
    visited = [0 for _ in range(N + 1)]
    visited[X] = 1
    queue = deque([X])
    while queue:
        Y = queue.popleft()
        for Z in link[Y]:
            if not visited[Z]:
                queue.append(Z)
                visited[Z] = 1
                cnt += 1
    return cnt


N, M = map(int, stdin.readline().split())
link = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, stdin.readline().split())
    link[b].append(a)

result = []
max_cnt = 0

for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    result.append([i, cnt])

for i, cnt in result:
    if cnt == max_cnt:
        print(i, end=' ')

