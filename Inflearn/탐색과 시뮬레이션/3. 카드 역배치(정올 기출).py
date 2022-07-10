from sys import stdin

# 1 - My Code
# nums = [i for i in range(1, 21)]
#
# for i in range(10):
#     ai, bi = map(int, stdin.readline().split())
#     nums[ai - 1:bi] = [nums[i] for i in range(bi - 1, ai - 2, -1)]
#
# for n in nums:
#     print(n, end=" ")


# 2 - Better
nums = list(range(21))
for _ in range(10):
    s, e = map(int, stdin.readline().split())
    for i in range((e - s + 1) // 2):
        nums[s + i], nums[e - i] = nums[e - i], nums[s + i]
nums.pop(0)
for n in nums:
    print(n, end=" ")
