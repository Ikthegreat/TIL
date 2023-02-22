Test_case = int(input())

for t in range(Test_case):
    string = input()
    N = len(string)
    new_string = [0] * N
    for i in range(N):
        if string[(N - 1) - i] == 'b':
            new_string[i] = 'd'
        elif string[(N - 1) - i] == 'd':
            new_string[i] = 'b'
        elif string[(N - 1) - i] == 'p':
            new_string[i] = 'q'
        elif string[(N - 1) - i] == 'q':
            new_string[i] = 'p'

    result = ''.join(new_string)

    print(f'#{t+1} {result}')
