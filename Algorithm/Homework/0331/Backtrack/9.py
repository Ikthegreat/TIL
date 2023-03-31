import sys
sys.stdin = open('9.txt', 'r')


def dfs(a, b, m, n):
    global result
    if m == 7:
        result.add(n)
        return
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= a + di < 4 and 0 <= b + dj < 4:
            dfs(a+di, b+dj, m+1, n+str(board[a][b]))


Test_case = int(input())

for t in range(Test_case):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')

    print(f'#{t+1} {len(result)}')
