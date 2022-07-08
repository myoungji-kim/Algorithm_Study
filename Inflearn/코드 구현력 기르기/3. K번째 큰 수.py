from sys import stdin

# 1 - My Code
# N, K = map(int, stdin.readline().split())
# cards = list(map(int, stdin.readline().split()))
# sums = []
#
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             temp = cards[i] + cards[j] + cards[k]
#             if temp not in sums:
#                 sums.append(temp)
#
# sums = sorted(sums, reverse=True)
# print(sums[K - 1])

# 2 - Better
N, K = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
sums = set()
for i in range(N):
    for j in range(i + 1, N):
        for m in range(j + 1, N):
            sums.add(cards[i] + cards[j] + cards[m])
sums = list(sums)
sums.sort(reverse=True)
print(sums[K-1])