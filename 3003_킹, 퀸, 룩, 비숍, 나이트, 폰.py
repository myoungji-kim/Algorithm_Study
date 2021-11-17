from sys import stdin

black = [1, 1, 2, 2, 2, 8]
white = list(map(int, stdin.readline().split()))
answer = []

for i in range(len(black)):
    answer.append(str(black[i]-white[i]))

print(" ".join(answer))