from sys import stdin

# 1 - My Code
# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x //= 10
#     return sum


# 2 - Better (문자열)
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
total = [0 for i in range(N)]

max, res = -1, -2147000000
for i in range(N):
    total[i] = digit_sum(nums[i])
    if total[i] > max:
        max = total[i]
        res = nums[i]

print(res)