from sys import stdin

def dfs(X, graph, visited):
    visited[X] = True

    for i in graph[X]:
        if not visited[i]:
            global count
            count += 1
            dfs(i, graph, visited)


N = int(stdin.readline())
link = int(stdin.readline())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for i in range(link):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, graph, visited)
print(count)



