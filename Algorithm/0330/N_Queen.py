def check(ti, tj):
    for di, dj in [(-1, -1), (-1, 0), (-1, 1)]:
        ni, nj = ti + di, tj + dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:
                return 0
            ni += di
            nj += dj
    return 1


def dfs(i, k):
    global count

    if i == k:
        count += 1
    else:
        for j in range(N):
            if check(i, j):
                board[i][j] = 1
                dfs(i+1, k)
                board[i][j] = 0


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    visited = [0] * N
    count = 0
    dfs(0, N)
    print(f'#{t+1} {count}')
