import math

F = str(math.factorial(int(input())))
N = len(F)-1
cnt = 0

for i in range(len(F)):
    if (int(F[N])==0):
        cnt += 1
        N -= 1
    else:
        print(cnt)
        exit()