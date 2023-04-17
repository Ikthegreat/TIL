Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [list(map(int, input().split())) for n in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    result = 0
    for i in range(N):
        for j in range(N):
            for a in range(4):
                ni = i + di[a]
                nj = j + dj[a]
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(arr[i][j] - arr[ni][nj])
    print(f'#{t+1} {result}')