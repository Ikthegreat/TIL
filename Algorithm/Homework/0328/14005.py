import sys
sys.stdin = open('14005.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container = sorted(container)[::-1]
    truck = sorted(truck)[::-1]
    result = [0] * M
    for i in range(M):
        for j in range(N):
            if truck[i] >= container[j]:
                result[i] = container[j]
                container[j] = 100
                break

    print(f'#{t+1} {sum(result)}')
