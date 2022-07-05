from sys import stdin

N = int(stdin.readline())
nums = []

for i in range(N):
    nums.append(int(stdin.readline()))

nums.sort()
for i in range(len(nums)):
    nums[i] *= len(nums)-i

print(max(nums))