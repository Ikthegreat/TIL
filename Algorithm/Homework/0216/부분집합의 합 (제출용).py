def power_set(nums):
    temp = []

    def backtrack(start, path):
        temp.append(path)

        for idx in range(start, len(nums)):
            backtrack(idx + 1, path + [nums[idx]])

    backtrack(0, [])

    return temp


Test_case = int(input())

for t in range(Test_case):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    A = power_set(A)
    count = 0
    for i in range(len(A)):
        if len(A[i]) == N and sum(A[i]) == K:
            count += 1
        else:
            continue

    print(f'#{t+1} {count}')
