# num_list = [1, 2, 3, 4, 5]
#
# sum_list = []
# for i in range(len(num_list) - 2):
#     sum_num = num_list[i : (i + 3)]
#     sum_list.append(sum_num)
#
# print(sum_list)

Test_case = int(input())

for t in range(Test_case):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    sum_list = []
    for i in range(len(num_list) - (M - 1)):
        sum_num = sum(num_list[i:(i + M)])
        sum_list.append(sum_num)

    answer = max(sum_list) - min(sum_list)
    print(f'#{t+1} {answer}')