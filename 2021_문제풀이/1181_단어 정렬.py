from sys import stdin

words = []

for i in range(int(stdin.readline())):
    words.append(stdin.readline().rstrip())

words = sorted(words)
words = sorted(set(words), key=len)

for i in range(len(words)):
    print(words[i])