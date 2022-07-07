from sys import stdin

T = int(stdin.readline())
for i in range(T):
    N, s, e, k = map(int, stdin.readline().split())
    temp = list(map(int, stdin.readline().split()))
    nums = sorted(temp[s - 1:e])
    # print("#", i + 1, sep="", end=" ")
    # print(nums[k-1])

    print("#%d %d" % (i + 1, nums[k - 1]))
