import sys
sys.stdin = open('Ladder2_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    Ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    direction = [[1, 0], [0, -1], [0, 1]]
                # 하강     좌회전    우회전
    direction_idx = 0

    start = []
    for s in range(len(Ladder[0])):
        if Ladder[s] == 1:
            start.append(s)

    for m in start:
    point_i = m
    point_j = 0
    move = 0
    result = []

        while True:
            if point_i == 99:
                result.append(move)
                break

            if Ladder[point_i][point_j - 1]:
                direction_idx = 1
                while True:
                    point_i += direction[direction_idx][0]
                    point_j += direction[direction_idx][1]
                    move += 1
                    if point_i == 99 or Ladder[point_i][point_j - 1] == 0:
                        break

            elif Ladder[point_i][point_j + 1]:
                direction_idx = 2
                while True:
                    point_i += direction[direction_idx][0]
                    point_j += + direction[direction_idx][1]
                    move += 1
                    if Ladder[point_i][point_j + 1] == 0:
                        break

            direction_idx = 0
            point_i += direction[direction_idx][0]
            point_j += direction[direction_idx][1]