import sys
sys.stdin = open('1.txt', 'r')


def perm(n, s):
    global result
    if n == N:
        if s == K:
            result += 1
        return

    perm(n+1, s+A[n])
    perm(n+1, s)


Test_case = int(input())

for t in range(Test_case):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0

    perm(0, 0)

    print(f'#{t+1} {result}')
