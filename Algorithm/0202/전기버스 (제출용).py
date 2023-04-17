# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
# 충전기가 살치된 M개의 정류장 번호

Test_case = int(input())

for t in range(Test_case):
    K, N, M = list(map(int, input().split()))
    charger_num = list(map(int, input().split()))
    charge = 0
    move = 0

    while move + K < N:
        for j in range(K, 0, -1):
            if (move + j) in charger_num:
                move += j
                charge += 1
                break
        else:
            charge = 0
            break

    if N - charger_num[-1] > K:
        charge = 0

    print(f'#{t+1} {charge}')