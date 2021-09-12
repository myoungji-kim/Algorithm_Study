import sys
A, B = sys.stdin.readline().split()

A = int(A)
B = int(B)

if (A>B):
    print(">")
elif (A<B):
    print("<")
elif (A==B):
    print("==")