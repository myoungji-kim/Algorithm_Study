from sys import stdin

n, m = map(int, stdin.readline().split())
balls = list(map(int, stdin.readline().split()))
ballLen = len(balls)
temp = []
answer = 0

for i in balls:
    cntNew = ballLen - balls.count(i)
    minus = len(temp) - temp.count(i)
    answer += cntNew - minus
    temp.append(i)

print(answer)