Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    count = [0] * 5
    prime_num = [2, 3, 5, 7, 11]
    for i in range(len(prime_num)):
        while True:
            if N % prime_num[i] == 0:
                N = N // prime_num[i]
                count[i] += 1
                continue
            else:
                break
    Answer = ' '.join(list(map(str, count)))
    print(f'#{t+1} {Answer}')