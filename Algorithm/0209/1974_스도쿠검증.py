import sys
sys.stdin = open("1974_스도쿠검증_input.txt", "r")

Test_case = int(input())

for t in range(Test_case):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = 0
    for i in range(9):
        column = [sudoku[x][i] for x in range(9)]
        if len(set(sudoku[i])) != 9:
            result = 0
            break
        elif len(set(column)) != 9:
            result = 0
            break
        else:
            result = 1

    three_by_three = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    three_by_three.append(sudoku[(3*a)+c][(3*b)+d])
            if len(set(three_by_three)) != 9:
                result = 0
                break
            else:
                three_by_three = []
                continue

    print(f'#{t+1} {result}')
