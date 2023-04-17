Test_case = int(input())

for t in range(1, Test_case+1):
    N = int(input())
    Box = list(map(int, input().split()))
    answer = 0
    for i in range(N-1):
        count = 0
        for j in range(i+1, N):
            if Box[i] > Box[j]:
                count += 1
        if answer < count:
            answer = count
    print(f'#{Test_case} {answer}')