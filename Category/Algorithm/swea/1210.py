from sys import stdin as s

txt = open('1210input.txt', 'rt')

for i in range(10):
    Test_case = int(txt.readline().strip())
    Ladder = []
    for j in range(100):
        Ladder.append(list(map(int, txt.readline().split())))

exit = []
for i in range(100):
    for j in range(100):
        if Ladder[i][j] == 2:
            exit.append(i)
            exit.append(j)

for i in range(99, 0, -1):
    for j in range(100):
        if Ladder[i][exit[1]-1] == 1:
            if Ladder[i][exit[1]-j] == 0:
                

        elif Ladder[i][exit[i]-1]:

        else:
            continue
                   

print(exit)