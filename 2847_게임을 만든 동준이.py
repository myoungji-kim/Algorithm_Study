from sys import stdin

score = []
cnt = 0

for i in range(int(stdin.readline())):
    score.append(int(stdin.readline()))

for i in range(len(score)-1, 0, -1):
    while score[i-1] >= score[i]:
        score[i-1] -= 1
        cnt += 1

print(cnt)