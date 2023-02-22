import sys
sys.stdin = open('password_input.txt', 'r')

Test_case = 10

for t in range(Test_case):
    _ = int(input())
    num_arr = list(map(int, input().split()))
    count = 0
    while True:
        num_arr[0] = num_arr[0] - count
        count = ((count + 1) % 6) + 1
        num_arr.append(num_arr.pop(0))
        if num_arr[-1] <= 0:
            num_arr[-1] = 0
            break

    print(f'#{t+1}', end=' ')
    print(*num_arr)