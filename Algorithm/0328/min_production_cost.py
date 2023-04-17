import sys
sys.stdin = open('min_production_cost.txt', 'r')


def perm(i, k):
    global result
    if i == k:
        temp = 0
        for n in range(N):
            temp += cost[p[n]][n]
        if result > temp:
            result = temp
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = j
                used[j] = 1
                perm(i+1, k)
                used[j] = 0


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * N
    used = [0] * N
    result = 2000
    perm(0, N)
    print(f'#{t+1} {result}')
