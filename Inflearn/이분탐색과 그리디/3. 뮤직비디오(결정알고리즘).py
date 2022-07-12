from sys import stdin


def check(size):
    cnt, sum = 1, 0
    for m in music:
        if m + sum > size:
            sum = m
            cnt += 1
        else:
            sum += m
    return cnt


N, M = map(int, stdin.readline().split())
music = list(map(int, stdin.readline().split()))
maxx = max(music)
lt, rt = 1, sum(music)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and check(mid) <= M:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
