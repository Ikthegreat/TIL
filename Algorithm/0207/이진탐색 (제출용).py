Test_case = int(input())

for t in range(Test_case):
    N, D = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    start = 0
    end = N - 1
    result = 0
    while True:
        middle = (start + end) // 2
        if start > end:
            break
        if D > arr[middle]:
            start = middle + 1
        elif D < arr[middle]:
            end = middle - 1
        elif arr[middle] == D:
            result = middle + 1
            break

    print(f'#{t+1} {result}')