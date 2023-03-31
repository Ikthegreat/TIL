import sys
sys.stdin = open('6.txt', 'r')


def btk(n, s):
    global result
    if s >= result:
        return
    if n >= 12:
        result = min(result, s)
        return
    # 일 이용권
    btk(n+1, s+(plan[n]*d1))
    if plan[n]:
        # 월 이용권
        btk(n+1, s+m1)
        # 3개월 이용권
        btk(n+3, s+m3)


Test_case = int(input())

for t in range(Test_case):
    d1, m1, m3, y1 = map(int, input().split())
    plan = list(map(int, input().split()))
    result = y1
    btk(0, 0)
    print(f'#{t+1} {result}')
