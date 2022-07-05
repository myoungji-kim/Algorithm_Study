from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

if N < K:
    print(0)
    exit()

sensor = list(map(int, stdin.readline().split()))
sensor.sort()

distance = [sensor[i + 1] - sensor[i] for i in range(N - 1)]
distance.sort()

for i in range(K - 1):
    distance.pop()

print(sum(distance))
