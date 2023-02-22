Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    carrot = list(map(int, input().split()))
    count_list = [1] * N
    level = 0
    for i in range(1, N):
        if carrot[i] > carrot[i-1]:
            count_list[level] += 1
        else:
            level += 1

    max_count = 0
    for j in count_list:
        if j > max_count:
            max_count = j
    
    print(f'#{t+1} {max_count}')