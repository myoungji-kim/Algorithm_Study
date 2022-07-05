from sys import stdin

n = int(stdin.readline())
word = stdin.readline().rstrip()
sum, cnt, m = 0, 0, 1234567891
for i in word:
    sum += (ord(i) - 96) * (31**cnt)
    cnt += 1

print(sum%m)
