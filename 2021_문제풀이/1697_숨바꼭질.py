from sys import stdin
from collections import deque

def bfs():
    queue = deque([N])

    while queue:
        v = queue.popleft()
        if v == K:
            print(dist[v])
            exit()
        for nv in (v - 1, v + 1, v * 2):
            if 0 <= nv <= 100000 and not dist[nv]:
                dist[nv] = dist[v] + 1
                queue.append(nv)


N, K = map(int, stdin.readline().split())

if N >= K:
    print(N - K)
    exit()

dist = [0] * 100001
bfs()
