from sys import stdin

A, B = map(int, stdin.readline().split())
nums = []
result = 0

for i in range(1, B + 1):
    for j in range(i):
        nums.append(i)

for i in range(A - 1, B):
    result += nums[i]

print(result)
