Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    turn = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    turn_idx = 0
    i_point = 0
    j_point = 0
    snail[i_point][j_point] = 1
    repeat = 0
    for x in range(2, N+1):
        i_point, j_point = i_point + turn[turn_idx][0], j_point + turn[turn_idx][1]
        snail[i_point][j_point] = x
        if x == N:
            turn_idx += 1

    move = N - 1
    for y in range(N+1, N ** 2 +1):
        while True:
            if repeat == 2:
                move -= 1
                continue
            for z in range(move):
                i_point, j_point = i_point + turn[turn_idx][0], j_point + turn[turn_idx][1]
                snail[i_point][j_point] = y
            turn_idx += 1
            repeat += 1

        # if count == 0:
        #     turn_idx += 1
        #     repeat += 1
        #     count = N - 1
        #     if repeat == 2:
        #         repeat = 0
        #         count -= 1
    if turn_idx == 3:
        turn_idx = 0

    for r in range(N):
        result = ' '.join(list(map(str, snail[r])))
        print(result)