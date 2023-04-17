Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    a_i = list(map(int, input().split()))
    result = [0] * 10
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if a_i[j] > a_i[j + 1]:
                a_i[j], a_i[j + 1] = a_i[j + 1], a_i[j]

    result_idx = 1
    for a in range(0, 5):
        result[result_idx] = a_i[a]
        result_idx += 2

    result_idx = 0
    for b in range((N - 1), (N - 6), -1):
        result[result_idx] = a_i[b]
        result_idx += 2

    answer = ' '.join(list(map(str, result)))

    print(f'#{t+1} {answer}')