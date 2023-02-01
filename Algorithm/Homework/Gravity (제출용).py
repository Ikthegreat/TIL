Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    Box = list(map(int, input().split()))
    Box_total = []
    Box_list = []
    for i in Box:
        while True:
            if len(Box_list) == 100:
                Box_total.append(Box_list)
                Box_list = []
                break
            if i != 0:
                i -= 1
                Box_list.append(1)
            else:
                Box_list.append(0)

    horizontal_total = []
    horizontal_list = []
    for x in range(100):
        for y in range(N):
            horizontal_list.append(Box_total[y][x])
        horizontal_total.append(horizontal_list)
        horizontal_list = []

    int_list = []
    for a in range(len(horizontal_total)):
        int_list.append(int(''.join(list(map(str, horizontal_total[a])))))

    new_list = []
    for b in int_list:
        new_list.append(list(map(int, str(b))))

    shoot = []
    count = 0
    for c in new_list:
        for d in c:
            if d == 0:
                count += 1
            else:
                continue
        shoot.append(count)
        count = 0

    print(f'#{t+1} {max(shoot)}')