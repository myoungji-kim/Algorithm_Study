from sys import stdin

nums = list(map(int, stdin.readline().split()))
nums.sort()
print(' '.join(map(str, nums)))