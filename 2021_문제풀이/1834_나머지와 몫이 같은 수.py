from sys import stdin

num = int(stdin.readline())
result = []

for i in range(num + 1, num * num, num + 1):
    result.append(i)

print(sum(result))
