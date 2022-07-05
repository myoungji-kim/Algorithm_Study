from sys import stdin

for _ in range(int(stdin.readline())):
    width, height, locate = map(int, stdin.readline().split())
    field = []
    answer = 0

    for i in range(height):
        field.append([0] * width)

    for i in range(locate):
        a, b = map(int, stdin.readline().split())
        field[b][a] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def dfs(x, y):
        if x <= -1 or x >= height or y <= -1 or y >= width:
            return False

        if field[x][y] == 1:
            field[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
        return False

    for i in range(height):
        for j in range(width):
            if dfs(i, j):
                answer += 1

    print(answer)
