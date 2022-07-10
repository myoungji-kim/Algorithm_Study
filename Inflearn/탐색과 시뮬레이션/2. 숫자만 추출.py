from sys import stdin

# 1 - My Code
# word = stdin.readline().rstrip()
# num = ''
#
# for w in word:
#     if w.isdigit():
#         num += w
#
# num = int(num)
# cnt = 1
# for i in range(1, num // 2 + 1):
#     if num % i == 0:
#         cnt += 1
#
# print(num, cnt, sep="\n")

# 2 - Better
word = stdin.readline().rstrip()
res = 0
for w in word:
    if w.isdecimal():
        res = res * 10 + int(w)

cnt = 1
for i in range(1, res // 2 + 1):
    if res % i == 0:
        cnt += 1

print(res, cnt, sep="\n")