from sys import stdin

N = int(stdin.readline())
graph = [[0 for _ in range(N + 2)]]
for _ in range(N):
    graph.append([0] + list(map(int, stdin.readline().split())) + [0])
graph.append([0 for _ in range(N + 2)])
visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0
for x in range(1, N + 1):
    for y in range(1, N + 1):
        isTop = 0
        if visited[x][y] != 1:
            for m in range(4):
                nx = x + dx[m]
                ny = y + dy[m]

                if graph[x][y] > graph[nx][ny]:
                    visited[nx][ny] = 1
                    isTop += 1

            # 최대값 여부 확인
            if isTop == 4:
                cnt += 1
                # visited[i][j] = 2

print(cnt)
