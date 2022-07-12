from sys import stdin


def Count(len):
    cnt = 0
    for x in nums:
        cnt += (x // len)
    return cnt


K, N = map(int, stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(K)]
s, e = 1, max(nums)
res = -1

while s <= e:
    mid = (s + e) // 2
    if Count(mid) >= N:
        res = mid
        s = mid + 1
    else:
        e = mid - 1

print(res)