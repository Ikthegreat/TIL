import sys
sys.stdin = open('오목판정_input.txt', 'r')


def check(arr):
    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):
            temp = '' + arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3] + arr[i+4][j+4]
            if temp == "o" * 5:
                return True
    else:
        return False


Test_case = int(input())
for t in range(Test_case):
    N = int(input())
    board = [''.join(input()) for _ in range(N)]
    board_ = [''.join(i) for i in zip(*board)]
    result = "NO"

    for b in board + board_:
        if 'o' * 5 in b:
            result = "YES"
            break
    else:
        if check(board) or check(board_[::-1]):
            result = "YES"
    print(f'#{t+1} {result}')