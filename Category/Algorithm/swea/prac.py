building_num = 100
building_level = list(map(int, ('0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 93 203 150 69 19 137 28 174 32 80 64 54 18 0 158 73 173 20 0 102 107 48 50 161 246 145 225 31 0 153 185 157 44 126 153 233 0 201 83 103 191 0 45 0 131 87 97 105 97 209 157 22 0 29 132 74 2 232 44 203 0 51 0 244 212 212 89 53 50 244 207 144 72 143 0 0').split()))

count_list = []
# if building_level[0] > (building_level[1]):
#     count_list.append(building_level[0] - (building_level[1]))

# elif building_level[building_num-1] > (building_level[building_num-2]):
#         count_list.append(building_level[building_num-1] - building_level[building_num-2])

left_big = 0
right_big = 0

for i in range(4, building_num):
    if (building_level[i-4]) >= (building_level[i-3]):
            left_big = (building_level[i-4])
        
    elif (building_level[i-4]) < (building_level[i-3]):
            left_big = (building_level[i-3])

    if (building_level[i]) >= (building_level[i-1]):
            right_big = (building_level[i])

    elif (building_level[i]) < (building_level[i-1]):
            right_big = (building_level[i-1])

    if left_big >= right_big:
        biggest = left_big

    elif right_big > left_big:
        biggest = right_big

    if building_level[i-2] > biggest:
        count_list.append((building_level[i-2]-biggest))

    elif building_level[i-2] <= biggest:
        continue

count = sum(count_list)

print(count)