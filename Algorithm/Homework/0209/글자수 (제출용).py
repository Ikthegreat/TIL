Test_case = int(input())

for t in range(Test_case):
    str1 = input()
    str2 = input()
    str_list = set(list(str1))
    count_list = [0] * len(str1)
    for i in range(len(str1)):
        for j in str2:
            if str1[i] == j:
                count_list[i] += 1
    result = 0
    for k in count_list:
        if result <= k:
            result = k

    print(f'#{t+1} {result}')