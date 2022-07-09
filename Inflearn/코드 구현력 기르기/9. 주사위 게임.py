from sys import stdin

# 1 - My Code
# N = int(stdin.readline())
# winner = -1
# for i in range(N):
#     nums = sorted(list(map(int, stdin.readline().split())))
#     res = -1
#
#     if sum(nums) == nums[0] * 3:
#         res = 10000 + (nums[0] * 1000)
#     elif nums[0] == nums[1]:
#         res = 1000 + (nums[0] * 100)
#     elif nums[1] == nums[2]:
#         res = 1000 + (nums[1] * 100)
#     else:
#         res = nums[-1] * 100
#
#     if res > winner:
#         winner = res
#
# print(winner)

# 2 - Better
N = int(stdin.readline())
res = 0
for i in range(N):
    tmp = sorted(stdin.readline().split())
    a, b, c = map(int, tmp)

    if a == b == c:
        money = 10000 + (a * 1000)
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100

    if money > res:
        res = money

print(res)