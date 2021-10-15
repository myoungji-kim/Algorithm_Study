from sys import stdin

words = list(stdin.readline().rstrip().split('-'))

for i in range(len(words)):
    print(words[i][0], end="")