from sys import stdin


def reverse(x):
    res = 0
    while x > 0:
        temp = x % 10
        res = res * 10 + temp
        x //= 10
    return res


def isPrime(x):
    if x < 2:
        return False

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
for n in nums:
    n = reverse(n)
    if isPrime(n):
        print(n, end=" ")
