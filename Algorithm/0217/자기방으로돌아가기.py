import sys
sys.stdin = open('room_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    room = [0] * 401
    N = int(input())
    for _ in range(N):
        start, end = map(int, input().split())
        if end < start:
            start, end = end, start

        if end % 2 == 1:
            end += 1

        if start % 2 == 0:
            start -= 1

        for i in range(start, end + 1):
            room[i] += 1

    result = max(room)
    print(f'#{t+1} {result}')