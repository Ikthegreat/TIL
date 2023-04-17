import sys
sys.stdin = open('5.txt', 'r')


def dfs(n, s):
    global result
    if s >= result:
        return
    if n == N:
        result = min(result, s)
        return

    for j in range(N):
        if not used[j]:
            used[j] = 1
            dfs(n+1, s+table[n][j])
            used[j] = 0


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = 100 * N
    used = [0] * N
    dfs(0, 0)
    print(f'#{t+1} {result}')
