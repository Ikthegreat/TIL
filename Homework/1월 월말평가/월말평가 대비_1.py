N = int(input())

lst = []

for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)
    else:
        continue

print(*lst)