def dfs(n, sm):
    global ans

    # 종료조건: n에 관련된, 항상 종료될 수 있는 조건으로!
    # 종료시점에서 정답처리!
    if n == N:
        if ans > sm:
            ans = sm
        return

    # n+1 하부함수 호출
    for j in range(N):
        if not v[j]:
            v[j] = 1  # 방문표시
            dfs(n + 1, sm + arr[n][j])
            v[j] = 0  # 사용후 반드시 clear!


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N
    v = [0] * N
    dfs(0, 0)
    print(f'#{test_case} {ans}')