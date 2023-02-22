# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# N = 3
#
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(i, j, ni, nj)
#
# # N = [[1, 2], [3, 4]]
# #
# # for i in N:
# #     for j in i:
# #         print(j)
import random

arr = [([0]*5)]*5

for i in range(5):
    for j in range(5):
        arr[i][j] = random.randrange(1, 26)

print(arr)