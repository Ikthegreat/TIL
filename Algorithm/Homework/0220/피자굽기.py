import sys
sys.stdin = open('pizza_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    for p in range(len(pizza)):
        pizza[p] = [pizza[p], p+1]
    stove = pizza[:N]
    pizza = pizza[N:]
    while True:
        stove[0][0] = stove[0][0] // 2
        if len(stove) == 1:
            result = stove[0][1]
            break
        if stove[0][0] == 0:
            stove.pop(0)
            if pizza:
                stove.append(pizza.pop(0))
        else:
            stove.append(stove.pop(0))

    print(f'#{t+1} {result}')
