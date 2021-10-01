from sys import stdin

nums = list(map(int, stdin.readline().split()))

for i in range(len(nums)):
    nums[i] *= nums[i]

print(sum(nums) % 10)
