T = int(input())
for t in range(T):
    Money = int(input())

    Money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count_list = []
    count = 0
    # while True:
    #     if Money == 0:
    #         break
    for i in Money_list:
        while True:
            if Money >= i:
                Money = Money - i
                count += 1
            elif Money < i:
                count_list.append(count)
                count = 0
                break

    print(f'#{t+1}')
    print(*count_list)