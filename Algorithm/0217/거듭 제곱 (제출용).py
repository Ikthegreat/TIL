import sys
sys.stdin = open('거듭제곱_input.txt', 'r')

Test_case = 10


def recursive_call(num, times):
    if times == 1:
        return num
    else:
        return recursive_call(num, times - 1) * num


for t in range(Test_case):
    T = int(input())
    N, M = map(int, input().split())
    count = 0
    print(f'#{T} {recursive_call(N, M)}')