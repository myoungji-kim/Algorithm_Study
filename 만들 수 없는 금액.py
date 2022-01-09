from sys import stdin

n = int(stdin.readline())
moneys = sorted(list(map(int, stdin.readline().split())))
answer = 1
for i in moneys:
    if answer < i:
        print(answer)
        break
    answer += i
