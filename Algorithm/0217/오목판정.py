import sys
sys.stdin = open('오목판정_input.txt', 'r')


def cross_check(arr):
    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):
            s = '' + arr[i][j] + arr[i + 1][j + 1] + arr[i + 2][j + 2] + arr[i + 3][j + 3] + arr[i + 4][j + 4]
            if s == "o" * 5:
                result = 'YES'
                return result
    else:
        return False


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = 'NO'

    for i in range(N):
        for j in range(N - 5 + 1):
            if board[i][j:j+5] == (['o'] * 5):
                result = 'YES'

    cross = []
    rev_cross = []

    for i in range(N):
        cross.append(board[i][i])
        rev_cross.append(board[i][N-1-i])

    for i in range(N - 5 + 1):
        if cross[i:i+5] == (['o'] * 5) or rev_cross[i:i+5] == (['o'] * 5):
            result = 'YES'

    for i in range(N):
        for j in range(N):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in range(N):
        for j in range(N - 5 + 1):
            if board[i][j:j+5] == (['o'] * 5):
                result = 'YES'

    print(f'#{t+1} {result}')