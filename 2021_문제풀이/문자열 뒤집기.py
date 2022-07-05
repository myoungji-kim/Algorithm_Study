from sys import stdin

nums = list(map(int, stdin.readline().rstrip()))
cntZeroToOne = 0
cntOneToZero = 0

for i in range(1, len(nums)):
    if not nums[i - 1] and nums[i]:  # 0 -> 1
        cntZeroToOne += 1
    elif nums[i - 1] and not nums[i]:  # 1 -> 0
        cntOneToZero += 1


if cntOneToZero >= cntZeroToOne:
    print(cntOneToZero)
else:
    print(cntZeroToOne)
