import sys
sys.stdin = open('화물도크.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    time = []
    for n in range(N):
        start, end = map(int, input().split())
        time.append((start, end))
    time.sort(key=lambda x: (x[1], x[0]))
    temp = 0
    result = 0
    for i in range(N):
        if time[i][0] >= temp:
            result += 1
            temp = time[i][1]

    print(f'#{t+1} {result}')
    print(time)