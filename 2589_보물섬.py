from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(stdin.readline().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    queue.append((nx, ny))
    return cnt - 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
