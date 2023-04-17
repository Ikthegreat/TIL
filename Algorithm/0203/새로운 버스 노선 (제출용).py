Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    bus_stop = [0] * 1001
    for n in range(N):
        bus_type, start, stop = list(map(int, input().split()))
        for current in range(start, stop + 1):
            # 일반 버스
            if bus_type == 1:
                bus_stop[current] += 1
            # 급행 버스
            elif bus_type == 2:
                if start % 2 == 0:
                    if current % 2 == 0 or current == start or current == stop:
                        bus_stop[current] += 1
                    else:
                        continue
                else:
                    if current % 2 == 1 or current == start or current == stop:
                        bus_stop[current] += 1
                    else:
                        continue
            # 광역 버스
            elif bus_type == 3:
                if start % 2 == 0:
                    if current % 4 == 0 or current == start or current == stop:
                        bus_stop[current] += 1
                    else:
                        continue
                else:
                    if current % 3 == 0 and current % 10 != 0:
                        bus_stop[current] += 1
                    elif current == start:
                        bus_stop[current] += 1
                    elif current == stop:
                        bus_stop[current] += 1
                    else:
                        continue
    Answer = max(bus_stop)
    print(f'#{t+1} {Answer}')