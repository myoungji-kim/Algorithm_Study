from sys import stdin

n = int(stdin.readline())
people = sorted(list(map(int, stdin.readline().split())))
cnt = 0
group = 0

for i in people:
    cnt += 1
    if i <= cnt:
        group += 1
        cnt = 0

print(group)
