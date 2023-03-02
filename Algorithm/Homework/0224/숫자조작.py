import sys
sys.stdin = open('number_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    num = list(map(int, input()))
    result = []
    stack = []

    while len(num) > 0:
        N = len(num)
        mini = maxi = num[0]
        min_idx = max_idx = 0

        for i in range(N):
            if (mini > num[i]) and (num[i] != 0):
                mini = num[i]
                min_idx = i
            if maxi < num[i]:
                maxi = num[i]
                max_idx = i

        if min_idx == 0:
            stack.append(num.pop(0))
        else:
            num[0], num[min_idx] = num[min_idx], num[0]
            result.append(stack + num)
            break
    else:
        result.append(stack)

    print(result)