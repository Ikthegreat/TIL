import sys
sys.stdin = open('4.txt', 'r')


def dfs(n, s):
    global result
    if n == N:
        if s >= B:
            result = min(result, abs(s-B))
        return

    dfs(n+1, s+crew[n])
    dfs(n+1, s)


Test_case = int(input())

for t in range(Test_case):
    N, B = map(int, input().split())
    crew = list(map(int, input().split()))
    result = 10000 * N
    dfs(0, 0)
    print(f'#{t+1} {result}')
