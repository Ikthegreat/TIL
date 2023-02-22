Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    count = [0] * N
    idx = 0
    num = list(map(int, input()))
    for i in num:
        if i == 0:
            idx += 1
        else:
            count[idx] += 1
    max_count = 0
    for j in count:
        if j > max_count:
            max_count = j
        else:
            continue
    print(f'#{t+1} {max_count}')