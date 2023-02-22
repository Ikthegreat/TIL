# 버스 노선은 N개
# i번째 버스 노선은 번호가 A 이상 B 이하인 모든 정류장만을 다니는 버스 노선
# P개의 정수
# j번째 정수는 C번 버스 정류장을 지나는 버스 노선의 개수

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    bus = [0] * 5001
    for n in range(N):
        A, B = list(map(int, input().split()))
        for i in range(A, B+1):
            bus[i] += 1
    P = int(input())
    require = []
    for p in range(P):
        C = int(input())
        require.append(bus[C])
        Answer = ' '.join(list(map(str, require)))
    print(f'#{t+1} {Answer}')
