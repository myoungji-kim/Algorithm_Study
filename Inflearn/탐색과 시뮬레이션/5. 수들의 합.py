from sys import stdin

# 1 - My Code (시간초과)
# N, M = map(int, stdin.readline().split())
# nums = list(map(int, stdin.readline().split()))
# sums = [nums[0]]
#
# for i in range(1, len(nums)):
#     sums.append(sums[-1] + nums[i])
#
# cnt = 0
#
# for i in range(N - 1, -1, -1):
#     for j in range(i, -1, -1):
#         if sums[i] - sums[j] == M or sums[i] == M:
#             cnt += 1
#             break
#         elif sums[i] - sums[j] > M:
#             break
# print(cnt)


# 2 - My Code
# N, M = map(int, stdin.readline().split())
# nums = list(map(int, stdin.readline().split()))
# lt, rt = 0, 0
# total = nums[0]
# cnt = 0
#
# while rt < N:
#     if total > M:
#         total -= nums[lt]
#         lt += 1
#     else:
#         if total == M:
#             cnt += 1
#         rt += 1
#         if rt != N:
#             total += nums[rt]
#
# print(cnt)


# 3 - Better (내가 2번째로 시도한게 더 깔끔해보이는데..!)
N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
lt, rt = 0, 1
total = nums[0]
cnt = 0

while True:
    if total < M:
        if rt < N:
            total += nums[rt]
            rt += 1
        else:
            break
    elif total == M:
        cnt += 1
        total -= nums[lt]
        lt += 1
    else:
        total -= nums[lt]
        lt += 1

print(cnt)