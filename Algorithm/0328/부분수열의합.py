import sys
sys.stdin = open('부분수열의합.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            if i & (1 << j):
                temp += arr[j]
        if temp == K:
            result += 1
    print(f'#{t+1} {result}')
