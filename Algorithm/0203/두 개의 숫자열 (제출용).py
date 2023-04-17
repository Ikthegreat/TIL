Test_case = int(input())

for t in range(Test_case):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        idx_multiple = [0] * M
        sum_multiple = [0] * (N - M + 1)
        for y in range(N - M + 1):
            for x in range(M):
                idx_multiple[x] = A[x + y] * B[x]
            sum_multiple[y] = sum(idx_multiple)
            idx_multiple = [0] * M
            Answer = max(sum_multiple)
            multiple = [0] * (N - M + 1)
    else:
        idx_multiple = [0] * N
        sum_multiple = [0] * (M - N + 1)
        for y in range(M - N + 1):
            for x in range(N):
                idx_multiple[x] = A[x] * B[x + y]
            sum_multiple[y] = sum(idx_multiple)
            idx_multiple = [0] * N
            Answer = max(sum_multiple)
            multiple = [0] * (M - N + 1)

    print(f'#{t+1} {Answer}')