Test_case = int(input())

for t in range(Test_case):
    D, A, B, F = list(map(int, input().split()))
    Time = D / (A + B)
    Answer = Time * F
    print(f'#{t+1} {Answer}')