import sys
sys.stdin = open('Elec_cart.txt', 'r')


def move(i, k):
    temp = 0
    if i == k-1:
        temp += room[0][p[0]] + room[p[-1]][0]
        for a in range(len(p) - 1):
            temp += room[p[a]][p[a+1]]
        result.append(temp)
    else:
        for j in range(0, k-1):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                move(i+1, k)
                used[j] = 0


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = list(range(1, N))
    room = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * (N - 1)
    used = [0] * N
    result = []
    move(0, N)

    print(f'#{t+1} {min(result)}')
