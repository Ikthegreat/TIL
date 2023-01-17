list(range(10))
two = []
for i in range(10):
    two.append(i)
    for j in two:
        if j % 2 == 0:
            j = True
        else:
            j = False
print(two)