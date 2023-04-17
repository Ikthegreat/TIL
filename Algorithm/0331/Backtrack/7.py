import sys
sys.stdin = open('7.txt', 'r')


def btk(n, c, p):
    global result
    if c >= result:
        return
    if n == N - 1:
        result = min(result, c)
        return
    if p > 0:
        btk(n+1, c, p-1)
    btk(n+1, c+1, battery[n]-1)


Test_case = int(input())

for t in range(Test_case):
    N, *battery = list(map(int, input().split()))
    result = 100
    btk(0, 0, battery[0])

    print(f'#{t+1} {result}')
