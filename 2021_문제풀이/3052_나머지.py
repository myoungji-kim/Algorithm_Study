from sys import stdin
num = [int(stdin.readline()) % 42 for i in range(10)]
print(len(set(num)))