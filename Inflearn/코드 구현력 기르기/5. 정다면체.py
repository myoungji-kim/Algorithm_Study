from sys import stdin

# 1 - My Code
# N, M = map(int, stdin.readline().split())
#
# dict = {}
# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if i + j in dict:
#             dict[i + j] += 1
#         else:
#             dict[i + j] = 1
#
# for i in dict:
#     if dict[i] == max(dict.values()):
#         print(i, end=" ")

# 2 - Better
N, M = map(int, stdin.readline().split())
cnt = [0 for i in range(N + M + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        cnt[i + j] += 1

max = -2147000000
for i in range(N + M + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(len(cnt)):
    if cnt[i] == max:
        print(i, end=" ")
