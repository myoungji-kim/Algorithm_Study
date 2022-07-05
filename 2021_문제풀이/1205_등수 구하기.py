from sys import stdin

N, S, P = map(int, stdin.readline().split())
if N == 0:
    print(1)
    exit()
scores = sorted(list(map(int, stdin.readline().split())), reverse=True)

if S <= scores[-1] and len(scores) == P:
    print(-1)

else:
    for i in range(1, len(scores)):
        if scores[i - 1] > S > scores[i]:
            print(i + 1)
            exit()
        elif scores[i - 1] == S:
            print(i)
            exit()

    print(len(scores)+1) if S < scores[-1] else print(len(scores))
