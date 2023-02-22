for test_case in range(10):

    building_num = int(input())
    building_level = list(map(int, input().split()))

    count_list = []

    left_big = 0
    right_big = 0

    for i in range(4, building_num):

        biggest = max([building_level[i], building_level[i-1], building_level[i-3], building_level[i-4]])

        if building_level[i-2] > biggest:
            count_list.append(building_level[i-2]-biggest)

        elif building_level[i-2] <= biggest:
            continue

    count = sum(count_list)

    print(f'#{test_case+1} {count}')