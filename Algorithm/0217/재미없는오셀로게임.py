import sys
sys.stdin = open('오셀로_input.txt', 'r')


def turn():







Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    board = [[0] * (N+2) for _ in range(N+2)]
    board[N//2][N//2], board[N//2+1][N//2], board[N//2][N//2+1], board[N//2+1][N//2+1] = 2, 1, 1, 2
    for _ in range(M):
        idx_i, idx_j, color = map(int, input().split())
        board[idx_i][idx_j] = color

    for i in range(N+2):
        print(board[i])
