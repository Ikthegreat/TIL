import sys
sys.stdin = open('input_ladder.txt', 'r')
sys.setrecursionlimit(10**7)

# for t in range(10):
Test_case = int(input())
Ladder = [list(map(int, input().split())) for _ in range(100)]

point = [0, 0]

for i in range(100):
    for j in range(100):
        if Ladder[i][j] == 2:
            point = [i, j]

# for r in range(100):
#     print(Ladder[r])


# def move(x):
#     if x[0] == 0:
#         return x[1]
#     else:
#         for a in range(x[0], -1, -1):
#             if Ladder[a][x[1] - 1] == 1:
#                 x = [a, x[1] - 1]
#                 for b in range(x[1], 0, -1):
#                     if Ladder[x[0]][b] == 0:
#                         x = [x[0], b + 1]
#                         move(x)
#             elif Ladder[a][x[1] + 1] == 1:
#                 x = [a, x[1] + 1]
#                 for c in range(x[1], 100):
#                     if Ladder[x[0]][c] == 0:
#                         x = [x[0], c - 1]
#                         move(x)

while True:
    if point[0] == 0:
        break
    i -= 1
    if point[i, (j - 1)] == 1:
        point = [i, j - 1]
    elif point[]


print(move(point))