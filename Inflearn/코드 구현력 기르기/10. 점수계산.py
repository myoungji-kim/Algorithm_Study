from sys import stdin

N = int(stdin.readline())
result = list(map(int, stdin.readline().split()))
cnt = 0
score = 0

for r in result:
    if r == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0

print(score)