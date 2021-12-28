from collections import deque
from sys import stdin


def bfs(X):
    queue = deque([X])
    visited = [0 for _ in range(N + 1)]
    visited[X] = 1

    while queue:
        x = queue.popleft()

        for i in family[x]:
            print("i:", i)
            print("x:", x)
            print("family[x]:",family[x])
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[x] + 1
                print("-result:", result)
                queue.append(i)
        print("////////////")

N = int(stdin.readline())
A, B = map(int, stdin.readline().split())
M = int(stdin.readline())
family = [[] for i in range(N + 1)]
result = [0 for i in range(N + 1)]

for i in range(M):
    X, Y = map(int, stdin.readline().split())
    family[X].append(Y)
    family[Y].append(X)

print("family:", family)

bfs(A)
print(result)
print(result[B]) if result[B] != 0 else print(-1)
