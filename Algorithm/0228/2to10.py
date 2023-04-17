import sys
sys.stdin = open('2to10.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    binary = list(map(int, input()))
    binary = binary[::-1]
    result = []
    for i in range(0, len(binary), 7):
        num = 0
        for j in range(i, i + 7):
            num += binary[j] * (2 ** (j % 7))
        result.append(num)

    print(f'#{t+1}', end=' ')
    print(*result[::-1])