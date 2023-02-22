N = int(input())

count = (1 + (4 * (N - 1)))

line = ['*'] * count
star = ' '.join(list(map(str, line)))


for i in range(count):
    if i == (count//2):
        for j in range(count):
            if j % 2 == 1:
                line[j] = ' '
                star = ' '.join(list(map(str, line)))
    else:
        line = ['*'] * count
        star = ' '.join(list(map(str, line)))
        print(star)