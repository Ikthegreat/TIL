Test_case = int(input())

for t in range(Test_case):
    P, P_a, P_b = list(map(int, input().split()))
    start = 1
    end = P
    A = 0
    while True:
        middle = int((start + end) / 2)
        if start > end:
            break
        if middle == P_a:
            break
        elif P_a < middle:
            end = middle
            A += 1
        elif P_a > middle:
            start = middle
            A += 1

    start = 1
    end = P
    B = 0
    while True:
        middle = int((start + end) / 2)
        if start > end:
            break
        if middle == P_b:
            break
        elif P_b < middle:
            end = middle
            B += 1
        elif P_b > middle:
            start = middle
            B += 1

    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'
    else:
        result = 0

    print(f'#{t+1} {result}')
