import sys
N = str(sys.stdin.readline().rstrip())
result = N
repeat = 0

if(len(N)==1):
    one = str(0)
    two = N
else:
    one = result[0]
    two = result[1]

final = 0
result = (int(one)+int(two))%10

while (int(final) != int(N)):
    repeat += 1
    one = two
    two = result
    result = (int(one)+int(two))%10
    final = str(one) + str(two)

if (repeat==0):
    repeat=1

print(repeat)