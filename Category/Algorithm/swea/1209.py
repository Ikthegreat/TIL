from sys import stdin as s

txt = open('1209input.txt', 'rt')

Test_case = int(txt.readline().strip())
num = []
for i in range(100):
    line = list(map(int, txt.readline().split()))
    num.append(line)

horizontal = []
for i in num:
    horizontal.append(sum(i))

horizontal_max = max(horizontal)

vertical = []
for i in num:
    for j in range(100):
        # vertical_sum = sum(i[j])
        # vertical.append(vertical_sum)
    print(vertical_sum)

