from sys import stdin

N, M = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))

for i in range(M):
    card.sort()
    card[0] += card[1]
    card[1] = card[0]

print(sum(card))
