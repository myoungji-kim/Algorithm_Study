from sys import stdin

nums = list(map(int, stdin.readline().rstrip()))
check = [0] * 9

for i in range(len(nums)):
    if nums[i] == 9:
        nums[i] = 6
    check[nums[i]] += 1

check[6] = (check[6] // 2) + (check[6] % 2)
print(max(check))
