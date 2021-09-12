from sys import stdin
n = int(stdin.readline())
f = [0]*(n+1)

for i in range(n+1):
    if (i==0):
        f[0] = 0
    elif (i==1):
        f[1] = 1
    else:
        f[i]=f[i-1]+f[i-2]

print(f[i])