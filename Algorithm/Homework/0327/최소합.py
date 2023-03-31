# import sys
# sys.stdin = open('min_sum.txt', 'r')
#
# Test_case = int(input())
#
# for t in range(Test_case):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     direction = [(-1, 0), (0, 1)]
#     move = (N * 2) - 1
#     si = sj = 0
#     count = board[si][sj]
#     for i in range(move):
#         for mi, mj in direction:
#             si += mi
#             sj += mj
#             if 0 <= si < N and 0 <= sj < N:
#                 count += board[si][sj]
#     print(count)


 v