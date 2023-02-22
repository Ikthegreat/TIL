Test_case = int(input())

for t in range(Test_case):
    N, K = list(map(int, input().split()))
    Arr = list(range(1, 13))
    Arr_len = len(Arr)
    result = 0
    for i in range(1 << Arr_len):
        sub_set = []
        for j in range(Arr_len):
            if i & (1 << j):
                sub_set.append(Arr[j])
        if len(sub_set) == N and sum(sub_set) == K:
            result += 1
    print(f'#{t+1} {result}')