from itertools import combinations
from sys import stdin

nums = []
test = []
result = []

for i in range(int(stdin.readline())):
    nums.append(list(map(int, stdin.readline().split())))
    test = list(combinations(nums[i], 3))
    for j in range(len(test)):
        test[j] = sum(test[j]) % 10
    result.append(max(test))

for i in range(len(result), 0, -1):
    if result[i - 1] == max(result):
        print(i)
        exit()