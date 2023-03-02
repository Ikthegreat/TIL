import sys
sys.stdin = open('이진수2.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = float(input())
    result = []
    while N > 0.0:
        N *= 2
        if N >= 1.0:
            N -= 1.0
            result.append(1)
        else:
            result.append(0)
        if len(result) > 12:
            result = 'overflow'
            break

    result = ''.join(map(str, result))

    print(f'#{t+1} {result}')
