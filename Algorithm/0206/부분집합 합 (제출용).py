Test_case = int(input())

for t in range(Test_case):
    arr = list(map(int, input().split()))
    N = len(arr)
    result = 0
    for i in range(1 << N):
        arr_list = []
        for j in range(N):
            if i & (1 << j):
                arr_list.append(arr[j])
                if sum(arr_list) == 0:
                    result = 1
    print(f'#{t+1} {result}')