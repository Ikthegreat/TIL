import sys
sys.stdin = open('secret_code.txt', 'r')

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
    sample_hexa = {
        'A': 10
        
    }

    stack = []
    temp = ''
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '0':
                temp += arr[i][j]
            else:
                if temp:
                    stack.append(temp)
                    temp = ''

    print(set(stack))

    for s in set(stack):


    # print(f'#{t+1} {result}')
