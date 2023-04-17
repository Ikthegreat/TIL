Test_case = int(input())

for t in range(Test_case):
    str1 = input()
    str2 = input()

    if str1 in str2:
        result = 1
    else:
        result = 0

    print(f'#{t+1} {result}')