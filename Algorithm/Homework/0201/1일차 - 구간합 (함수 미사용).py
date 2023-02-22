Test_case = int(input())

for t in range(Test_case):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    sum_list = [0]*(len(num_list) - (M - 1))
    for i in range(len(num_list) - (M - 1)):
        sum_num = 0
        for j in range(i, i+M):
            sum_num += num_list[j]
        sum_list[i] = sum_num

    min_num = sum_list[0]
    max_num = sum_list[0]
    for k in sum_list:
        if min_num > k:
            min_num = k
        if max_num < k:
            max_num = k
        else:
            continue

    answer = max_num - min_num
    print(f'#{t+1} {answer}')