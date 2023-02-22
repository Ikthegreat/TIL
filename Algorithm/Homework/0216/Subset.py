A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
subset = [[]]

for i in A:
    for L in range(len(subset)):
        subset.append(subset[L] + [i])

print(subset)