import sys
sys.stdin = open('Baby_gin.txt', 'r')


def check(p1, p2):
    for a in range(10):
        if p1[a] == 3:
            result[0] = 1
        elif p1[a] and p1[a+1] and p1[a+2]:
            result[0] = 1
    for b in range(10):
        if p2[b] == 3:
            result[1] = 1
        elif p2[b] and p2[b+1] and p2[b+2]:
            result[1] = 1


Test_case = int(input())

for t in range(Test_case):
    arr = list(map(int, input().split()))
    P1 = [0] * 12
    P2 = [0] * 12
    result = [0, 0]
    for i in range(len(arr)):
        if i % 2 == 0:
            P1[arr[i]] += 1
        else:
            P2[arr[i]] += 1
        check(P1, P2)
        if result:
            if result[0] == 1 and result[1] == 1:
                print(f'#{t+1} 0')
                break
            elif result[0] == 1:
                print(f'#{t+1} 1')
                break
            elif result[1] == 1:
                print(f'#{t+1} 2')
                break
    else:
        print(f'#{t+1} 0')
