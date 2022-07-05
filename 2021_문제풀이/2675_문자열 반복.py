from sys import stdin

for i in range(int(stdin.readline())):
    N, M = stdin.readline().split()
    for j in range(len(M)):
        print(M[j]*int(N), end="")
    print("")