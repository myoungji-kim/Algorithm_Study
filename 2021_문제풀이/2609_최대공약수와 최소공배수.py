import math
from sys import stdin
num1, num2 = map(int, stdin.readline().split())

def lcm(num1, num2):
    return num1 * num2 / math.gcd(num1, num2)

print(math.gcd(num1, num2))
print(round(lcm(num1, num2)))