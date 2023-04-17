Test_case = int(input())

for t in range(Test_case):
    K, N, M = list(map(int, input().split()))
    bus_stop_num = list(map(int, input().split()))
    Answer = 0

for i in range(len(bus_stop_num)):
    if (bus_stop_num[i] - bus_stop_num[i-1]) > K:
        Answer = 0
        break
    else:
        Answer = N // K
        for j in range(len(bus_stop_num)):
            if (bus_stop_num[j] - bus_stop_num[j-2]) > N / K
                Answer += 1
            else:
                continue

if bus_stop_num[0] > K:
    Answer = 0
elif N - bus_stop_num[-1] > K:
    Answer = 0

print(f'#{t+1} {Answer}')