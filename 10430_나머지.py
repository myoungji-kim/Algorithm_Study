import sys
A, B, C = sys.stdin.readline().split()
A = int (A)
B = int (B)
C = int (C)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)