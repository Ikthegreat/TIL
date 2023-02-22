Test_case = int(input())


def power_set(nums):
    temp = []

    def backtrack(start, path):
        temp.append(path)

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])

    return temp


for t in range(Test_case):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = power_set(numbers)
    result = 0
    for i in range(len(numbers)):
        if sum(numbers[i]) == K:
            result += 1
        else:
            continue

    print(f'#{t+1} {result}')
