import sys

N, M = map(int, sys.stdin.readline().split())

wood = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(wood)

while start <= end:
    middle = (start + end) // 2
    take = 0

    for i in range(N):
        if wood[i] > middle:
            take += (wood[i] - middle)

    if take > M:
        bottom = middle + 1
    elif take < M:
        top = middle - 1

print(middle)
