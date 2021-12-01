from sys import stdin


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    if b % a:
        return gcd(b % a, a)
    else:
        return a


for i in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    print(lcm(A, B))
