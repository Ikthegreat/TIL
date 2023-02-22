Test_case = int(input())

for t in range(Test_case):
    A, B = map(str, input().split())
    if len(A) < len(B):
        result = 0
        break
    A = list(A)
    B = list(B)
    fast_count = 0
    normal_count = 0
    for i in range(len(A) - len(B) + 1):
        if A[i:i + len(B)] == B:
            fast_count += 1
            A[i:i + len(B)] = [0] * len(B)

    normal_count = len(A) - (fast_count * len(B))

    result = fast_count + normal_count

    print(f'#{t+1} {result}')