from sys import stdin
X, Y = stdin.readline().split()
sum = str(int(X[::-1]) + int(Y[::-1]))
print(int(sum[::-1]))