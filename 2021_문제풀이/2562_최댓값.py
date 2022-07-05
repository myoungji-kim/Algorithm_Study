import sys
N = []

while True:
    try:
        N.append(int(sys.stdin.readline()))
    except:
        break

print(max(N))
print(N.index(max(N))+1)