from sys import stdin

N = int(stdin.readline())
score = list(map(int, stdin.readline().split()))
top = max(score)
aver = 0

for i in range(len(score)):
    score[i] = score[i]/top*100
    aver += score[i]

print(aver/len(score))