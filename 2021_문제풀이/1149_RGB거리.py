from sys import stdin


def dp(min1, min2, i, p):
    return min(house[i - 1][min1], house[i - 1][min2]) + house[i][p]


house = [list(map(int, stdin.readline().split())) for i in range(int(stdin.readline()))]

for i in range(1, len(house)):
    house[i][0] = dp(1, 2, i, 0)
    house[i][1] = dp(0, 2, i, 1)
    house[i][2] = dp(0, 1, i, 2)

print(min(house[-1][0], house[-1][1], house[-1][2]))
