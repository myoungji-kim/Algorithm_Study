from sys import stdin

nums = list(map(int, stdin.readline().rstrip()))
result = nums[0]

for i in range(1, len(nums)):
    if nums[i - 1] == 0 or nums[i - 1] == 1:
        result += nums[i]
    else:
        result *= nums[i]

print(result)
