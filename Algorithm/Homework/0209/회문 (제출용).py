Test_case = int(input())

for t in range(Test_case):
    N, M = list(map(int, input().split()))
    board = [list(input()) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N - M + 1):
            if board[i][j:j+M] == board[i][j:j+M][::-1]:
                result = board[i][j:j+M]
                break
            else:
                continue

    turn_board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            turn_board[x][y] = board[y][x]

    for i in range(N):
        for j in range(N - M + 1):
            if turn_board[i][j:j + M] == turn_board[i][j:j + M][::-1]:
                result = turn_board[i][j:j + M]
                break
            else:
                continue

    Answer = ''.join(list(map(str, result)))

    print(f'#{t+1} {Answer}')