Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]

    arr[1][1] = 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    for i in range(1, N+1):
        for j in range(1, i+1):
            print(arr[i][j], end=' ')
        print()