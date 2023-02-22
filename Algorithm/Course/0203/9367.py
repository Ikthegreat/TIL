Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    count = [1] * N
    idx = 0
    carrot = list(map(int, input().split()))
    for i in range(1, N):
        if carrot[i] > carrot[i-1]:
            count[idx] += 1
        else:
            idx += 1
    max_count = 0
    for j in count:
        if j > max_count:
            max_count = j
        else:
            continue

    print(f'#{t+1} {max_count}')