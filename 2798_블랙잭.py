from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))
newCard = list(combinations(card, 3))

for i in range(len(newCard)):
    newCard[i] = sum(newCard[i])

newCard.sort()

while True:
    out = newCard.pop()
    if out <= M:
        print(out)
        exit()