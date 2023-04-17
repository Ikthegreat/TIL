Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    turn = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    turn_idx = 0
    i = 0
    j = 0
    for count in range(1, N * N + 1):
        snail[i][j] = count
        i_move, j_move = i + turn[turn_idx][0], j + turn[turn_idx][1]
        if (0 <= i_move < N) and (0 <= j_move < N) and (snail[i_move][j_move] == 0):
            i, j = i_move, j_move
        else:
            turn_idx = (turn_idx + 1) % 4
            i, j = i + turn[turn_idx][0], j + turn[turn_idx][1]

    print(f'#{t + 1}')
    for r in range(N):
        result = ' '.join(list(map(str, snail[r])))
        print(result)