Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    a = b = c = d = e = 0
    while True:
        if N == 1:
            break
        elif N % 2 == 0:
            N = N // 2
            a += 1
            continue
        elif N % 3 == 0:
            N = N // 3
            b += 1
            continue
        elif N % 5 == 0:
            N = N // 5
            c += 1
            continue
        elif N % 7 == 0:
            N = N // 7
            d += 1
            continue
        elif N % 11 == 0:
            N = N // 11
            e += 1
            continue
    print(f'#{t+1} {a} {b} {c} {d} {e}')