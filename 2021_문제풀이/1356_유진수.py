from sys import stdin

nums = list(stdin.readline().rstrip())

for i in range(1, len(nums)):
    newFront = 1
    newBack = 1

    front = (''.join(nums[:i]))
    for j in front:
        newFront *= int(j)
    back = (''.join(nums[i:]))
    for j in back:
        newBack *= int(j)

    if newFront == newBack:
        print("YES")
        exit()

print("NO")
