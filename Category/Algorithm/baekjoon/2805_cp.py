import sys

N, M = map(int, sys.stdin.readline().split())

wood = list(map(int, sys.stdin.readline().split()))

total = sum(wood)

cut = (total - M) / N

print(cut)

# while True:
#     take = 0
#
#     if take >= M:
#         break
#     else:
#         cut -= 1

print(cut)
