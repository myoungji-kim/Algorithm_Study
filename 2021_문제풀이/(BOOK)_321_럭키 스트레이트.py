from sys import stdin

nums = list(map(int, stdin.readline().rstrip()))
left, right = 0, 0

for i in range(len(nums)):
    if i < len(nums)/2:
        left += nums[i]
    else:
        right += nums[i]

print("LUCKY") if left == right else print("READY")