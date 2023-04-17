Test_case = int(input())

for t in range(Test_case):
    N, K = list(map(int, input().split()))
    puzzle = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0] * (N+2))

    result = 0
    for i in range(N+2):
        for j in range(N - K + 1):
            if puzzle[i][j:j+K+2] == [0] + [1] * K + [0]:
                result += 1

    for i in range(N+2):
        for k in range(N+2):
            if i < k:
                puzzle[i][k], puzzle[k][i] = puzzle[k][i], puzzle[i][k]
        for j in range(N - K + 1):
            if puzzle[i][j:j+K+2] == [0] + [1] * K + [0]:
                result += 1

    print(f'#{t+1} {result}')