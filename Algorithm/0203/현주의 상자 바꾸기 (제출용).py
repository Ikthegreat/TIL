Test_case = int(input())

for t in range(Test_case):
    N, Q = list(map(int, input().split()))
    Box = [0] * N
    for q in range(Q):
        L, R = list(map(int, input().split()))
        for i in range(L-1, R):
            Box[i] = q+1
    Answer = ' '.join(list(map(str, Box)))
    print(f'#{t+1} {Answer}')
