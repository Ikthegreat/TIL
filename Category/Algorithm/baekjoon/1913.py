N = int(input())

snail = [[0] * N for _ in range(N)]

center = N // 2

num = 1
num_count = 0

snail[center][center] = num

di = center
dj = center

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
move_idx = 0

repeat = 0

while True:
    if di <= 0 or di >= N-1 or dj <= 0 or dj >= N-1:
        break
    num += 1
    di, dj = di + move[move_idx][0], dj + move[move_idx][1]
    snail[di][dj] = num
    repeat += 1
    move_idx += 1
        # repeat = 0
    if move_idx == 3:
        move_idx = 0
        continue


for r in range(N):
    print(snail[r])
