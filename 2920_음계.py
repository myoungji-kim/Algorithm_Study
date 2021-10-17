from sys import stdin

nums = list(stdin.readline().split())
result = 0

for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        result += 1
    else:
        result -= 1

if result == 7:
    print("ascending")
elif result == -7:
    print("descending")
else:
    print("mixed")
