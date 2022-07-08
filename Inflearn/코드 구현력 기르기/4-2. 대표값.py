from sys import stdin

# 1 - My Code
# N = int(stdin.readline())
# scores = list(map(int, stdin.readline().split()))
# minus = [0] * N
# aver = round(sum(scores) / N)
#
# for i in range(N):
#     minus[i] = abs(scores[i] - aver)
#
# temp = set()
# for i in range(N):
#     if min(minus) == minus[i]:
#         temp.add(scores[i])
#
# print(aver, scores.index(max(temp)) + 1)

# 2 - Better
N = int(stdin.readline())
scores = list(map(int, stdin.readline().split()))
aver = int((sum(scores) / N) + 0.5)
min = 2147000000

for idx, x in enumerate(scores):
    tmp = abs(x - aver)
    if tmp < min:
        min = tmp
        score = x
        result = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            result = idx + 1

print(aver, result)