import sys
sys.stdin = open('14.txt', 'r')


def dfs(n):
    global result
    # 가지치기 : n 회, 특정 값이 중복해서 나온다면 다시 처리 필요
    if (n + int(''.join(num))*100) in visited:
        return
    visited[(n + int(''.join(num))*100)] = 1

    if n == c:
        result = max(result, int(''.join(num)))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            num[i], num[j] = num[j], num[i]
            dfs(n+1)
            num[i], num[j] = num[j], num[i]


Test_case = int(input())

for t in range(Test_case):
    num, c = map(int, input().split())
    num = list(str(num))
    L = len(num)
    visited = {}

    result = 0
    dfs(0)
    print(f'#{t+1} {result}')
