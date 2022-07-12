from sys import stdin

# 1 - My Code
# graph = [list(map(int, stdin.readline().split())) for _ in range(7)]
#
#
# def check(nums):
#     for i in range(len(nums) // 2):
#         if nums[i] != nums[-(i + 1)]:
#             return 0
#     else:
#         return 1
#
#
# cnt = 0
# for i in range(7):
#     for j in range(3):
#         nums1, nums2 = '', ''
#         for k in range(5):
#             nums1 += str(graph[i][j + k])
#             nums2 += str(graph[j + k][i])
#         cnt += check(nums1) + check(nums2)
#
# print(cnt)


# 2 - Better
board = [list(map(int, stdin.readline().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1
print(cnt)