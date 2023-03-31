import sys
sys.stdin = open('15674.txt', 'r')


def calculate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a / b)


def dfs(i, k):
    global min_result, max_result
    if i == N:
        if max_result < k:
            max_result = k
        if min_result > k:
            min_result = k
        return

    for j in range(4):
        if ops[j]:
            ops[j] -= 1
            dfs(i+1, calculate(k, nums[i+1], j))
            ops[j] += 1


Test_case = int(input())

for t in range(Test_case):
    N = int(input()) - 1
    ops = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    s = nums[0]

    max_result = -100000000
    min_result = 100000000
    dfs(0, s)
    print(f'#{t+1} {max_result - min_result}')
