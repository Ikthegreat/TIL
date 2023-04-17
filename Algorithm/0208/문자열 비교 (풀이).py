Test_case = int(input())

for t in range(Test_case):
    str1 = input()
    str2 = input()
    M = len(str1)
    N = len(str2)
    result = 0

    for i in range(N - M + 1):
        for j in range(M):
            if str1[j] != str2[i + j]:
                break
        else:
            result = 1
            break

    print(f'#{t+1} {result}')