from sys import stdin

# 1 - My Code
# N = int(stdin.readline())
# nums = [1 for i in range(N + 1)]
# nums[0], nums[1] = 0, 0
#
# for i in range(2, N):
#     if nums[i] == 1:
#         n = 2
#         while i * n <= N:
#             nums[i * n] = 0
#             n += 1
#
# print(nums.count(1))

# 2 - Better
N = int(stdin.readline())
nums = [0 for i in range(N + 1)]
cnt = 0
for i in range(2, N + 1):
    if nums[i] == 0:
        cnt += 1
        for j in range(i, N + 1, i):
            nums[j] = 1

print(cnt)
