from collections import deque
from sys import stdin

m, n = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            queue.append((x, y))

bfs()

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            print(-1)
            exit()

print(max(map(max, graph))-1)
