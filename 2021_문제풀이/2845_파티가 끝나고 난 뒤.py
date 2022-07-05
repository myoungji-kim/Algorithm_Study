from sys import stdin

L, P = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
correct = L * P

for i in range(5):
    print(nums[i] - correct, end=" ")
