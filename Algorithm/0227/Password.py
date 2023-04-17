import sys
sys.stdin = open('password_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    sample = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    end = 0
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                end = (i, j)
                break

    code = arr[end[0]][(end[1] - 55): (end[1] + 1)]

    result = []
    for i in range(0, len(code), 7):
        result.append(sample[code[i: i+7]])

    sample = []
    for j in range(len(result)):
        if j % 2 == 0 and j != len(result):
            sample.append(result[j] * 3)
        else:
            sample.append(result[j])

    if sum(sample) % 10 == 0:
        result = sum(result)
    else:
        result = 0

    print(f'#{t+1} {result}')
