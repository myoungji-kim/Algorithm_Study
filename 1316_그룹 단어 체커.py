from sys import stdin

count = 0
repeat = int(stdin.readline())
check = [True] * repeat

for i in range(repeat):
    alpha = {}
    words = stdin.readline().rstrip()
    for j in range(len(words)):
        if words[j] in alpha:
            test = j - alpha[words[j]]
            if test != 1:
                check[i] = False
            else:
                alpha[words[j]] = j
        else:
            count += 1
            alpha[words[j]] = j

print(check.count(True))
