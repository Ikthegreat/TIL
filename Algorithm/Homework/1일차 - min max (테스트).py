Test_case = int(input())

for t in range(Test_case):
    number = int(input())
    num_list = list(map(int, input().split()))
    min_num = num_list[0]
    max_num = num_list[0]
    for i in num_list:
        if min_num >= i:
            min_num = i
        if max_num <= i:
            max_num = i
        else:
            continue

    print(f'#{t+1} {max_num - min_num}')