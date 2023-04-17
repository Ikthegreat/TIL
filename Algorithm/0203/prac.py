A = [1, 5, 3]
B = [3, 6, -7, 5, 4]
N = 3
M = 5

idx_multiple = [0] * N
sum_multiple = [0] * (M - N + 1)
for y in range(M - N + 1):
    for x in range(N):
        idx_multiple[x] = A[x] * B[x+y]
    sum_multiple[y] = sum(idx_multiple)
    print(sum_multiple)
    idx_multiple = [0] * N
    Answer = max(sum_multiple)
    multiple = [0] * (M - N + 1)
print(Answer)
