Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [[1]*(i+1) for i in range(N)]
    for i in range(2, N):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{t+1}')
    for num in arr:
        print(*num)