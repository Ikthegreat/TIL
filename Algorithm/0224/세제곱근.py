Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    for i in range(int(N ** (1/3)) - 1, int(N ** (1/3)) + 2):
        if i ** 3 == N:
            X = i
            break
    else:
        X = -1

    print(f'#{t+1} {X}')
