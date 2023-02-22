Test_case = int(input())

for t in range(Test_case):
    A, B = map(str, input().split())
    if len(A) < len(B):
        result = 0
        break
    A = list(A)
    B = list(B)
    count = 0
    for i in range(len(A) - len(B) + 1):
        if A[i:i + len(B)] == B:
            count += 1
            A[i:i + len(B)] = '' * len(B)

    result = len(A) + count

    print(f'#{t+1} {result}')