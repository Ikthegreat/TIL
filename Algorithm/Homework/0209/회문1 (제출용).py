Test_case = 10

for t in range(Test_case):
    N = int(input())
    board = [input() for _ in range(8)]

    count = 0
    for i in range(8):
        for j in range(8 - N + 1):
            if board[i][j:j+N] == board[i][j:j+N][::-1]:
                count += 1
            else:
                continue

    turn_board = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            turn_board[i][j] = board[j][i]

    for i in range(8):
        for j in range(8 - N + 1):
            if turn_board[i][j:j+N] == turn_board[i][j:j+N][::-1]:
                count += 1
            else:
                continue

    # for i in range(8):
    #     for j in range(8 - N + 1):
    #         vertical_list = []
    #         for k in range(N):
    #             vertical_list.append(board[k+N][i])
    #         if vertical_list == vertical_list[::-1]:
    #             count += 1
    #         else:
    #             continue

    print(f'#{t+1} {count}')