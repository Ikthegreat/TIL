for test_case in range(10):

    building_num = int(input())
    building_level = list(map(int, input().split()))

    count_list = []
    # if building_level[0] > (building_level[1]):
    #     count_list.append(building_level[0] - (building_level[1]))

    # elif building_level[building_num-1] > (building_level[building_num-2]):
    #         count_list.append(building_level[building_num-1] - building_level[building_num-2])

    left_big = 0
    right_big = 0

    for i in range(4, building_num):
        # if (building_level[i-4]) >= (building_level[i-3]):
        #         left_big = (building_level[i-4])
            
        # elif (building_level[i-4]) < (building_level[i-3]):
        #         left_big = (building_level[i-3])

        # if (building_level[i]) >= (building_level[i-1]):
        #         right_big = (building_level[i])

        # elif (building_level[i]) < (building_level[i-1]):
        #         right_big = (building_level[i-1])

        # if left_big >= right_big:
        #     biggest = left_big

        # elif right_big > left_big:
        #     biggest = right_big

        biggest = max([building_level[i], building_level[i-1], building_level[i-3], building_level[i-4]])

        if building_level[i-2] > biggest:
            count_list.append(building_level[i-2]-biggest)

        elif building_level[i-2] <= biggest:
            continue

    count = sum(count_list)

    print(f'#{test_case+1} {count}')