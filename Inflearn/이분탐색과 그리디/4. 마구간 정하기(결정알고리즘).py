from sys import stdin


def check(length):
    cnt, tmp = 1, locate[0]
    for l in locate:
        if l - tmp >= length:
            cnt += 1
            tmp = l
    return cnt


N, C = map(int, stdin.readline().split())
locate = sorted([int(stdin.readline()) for _ in range(N)])
lt, rt = locate[0], locate[-1]
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) < C:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1

print(res)
