from sys import stdin

exp = stdin.readline().split('-')
num = []

for i in exp:
    cnt = 0
    plus = i.split('+')
    for j in plus:
        cnt += int(j)
    num.append(cnt)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)