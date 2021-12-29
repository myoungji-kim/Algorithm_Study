from sys import stdin

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
distance = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            distance[i] = max(distance[i], distance[j]+1)

print(max(distance))
