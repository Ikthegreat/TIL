import sys
sys.stdin = open('정사각형판정_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = 'yes'

    left_top 

    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                left_top = [i, j]
                break

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if board[i][j] == '#':
                left_top = [i, j]

    for x in range(left_top[0], right_bottom[0]+1):
        for y in range(left_top[1], right_bottom[1]+1):
            if board[y][x] != '#':
                result = 'no'
                break
            elif right_bottom[0] - left_top[0] != right_bottom[1] - left_top[1]:
                result = 'no'
                break
        if result == 'no':
            break

    print(f'#{t+1} {result}')