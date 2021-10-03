from sys import stdin

nums = []

for i in range(7):
    new = int(stdin.readline())
    if new % 2 != 0:
        nums.append(new)

if len(nums) == 0:
    print(-1)
else:
    print(sum(map(int, nums)))
    print(min(nums))
