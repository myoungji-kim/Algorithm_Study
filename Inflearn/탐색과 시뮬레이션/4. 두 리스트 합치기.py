from sys import stdin
# 1 - My Code
# n = int(stdin.readline())
# nList = list(map(int, stdin.readline().split()))
# m = int(stdin.readline())
# mList = list(map(int, stdin.readline().split()))
# nums = sorted(nList + mList)
#
# for n in nums:
#     print(n, end=" ")


# 2 - My Code
# n = int(stdin.readline())
# nList = deque(list(map(int, stdin.readline().split())))
# m = int(stdin.readline())
# mList = deque(list(map(int, stdin.readline().split())))
# res = []
#
# for i in range(n+m):
#     if len(nList) > 0 and len(mList) > 0:
#         if nList[0] <= mList[0]:
#             res.append(nList.popleft())
#         else:
#             res.append(mList.popleft())
#     elif len(nList) > 0:
#         res.append(nList.popleft())
#     else:
#         res.append(mList.popleft())
#
# for n in res:
#     print(n, end=" ")


# 3 - My Code
# n = int(stdin.readline())
# nList = list(map(int, stdin.readline().split()))
# m = int(stdin.readline())
# mList = list(map(int, stdin.readline().split()))
# p1, p2 = 0, 0
# res = []
#
# for i in range(n + m):
#     if p1 >= n:
#         res.append(mList[p2])
#         p2 += 1
#     elif p2 >= m:
#         res.append(nList[p1])
#         p1 += 1
#     else:
#         if nList[p1] <= mList[p2]:
#             res.append(nList[p1])
#             p1 += 1
#         else:
#             res.append(mList[p2])
#             p2 += 1
#
# for n in res:
#     print(n, end=" ")


# 4 - Better
n = int(stdin.readline())
nList = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
mList = list(map(int, stdin.readline().split()))
p1, p2 = 0, 0
res = []

while p1 < n and p2 < m:
    if nList[p1] <= mList[p2]:
        res.append(nList[p1])
        p1 += 1
    else:
        res.append(mList[p2])
        p2 += 1

if p1 < n:
    res += nList[p1:]
else:
    res += mList[p2:]

for n in res:
    print(n, end=' ')