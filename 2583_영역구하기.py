import sys
from sys import stdin

sys.setrecursionlimit(100000)

M, N, K = map(int, stdin.readline().split())
dp = [[0 for i in range(N)] for j in range(M)]

for _ in range(K):
    X1, Y1, X2, Y2 = map(int, stdin.readline().split())
    for i in range(Y1, Y2):
        for j in range(X1, X2):
            dp[i][j] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global size
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < M and -1 < ny < N:
            if dp[nx][ny] == 0:
                dp[nx][ny] = 1
                dfs(nx, ny)
    size += 1


global size
sizeList = []
for i in range(M):
    for j in range(N):
        if dp[i][j] == 0:
            size = 0
            dp[i][j] = 1
            dfs(i, j)
            sizeList.append(size)

print(len(sizeList))
print(' '.join(str(s) for s in sorted(sizeList)))
