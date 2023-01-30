N_M_ = list(map(int, input().split()))

A = []
for i in range(N_M_[0]):
    A.append(list(map(int, input().split())))

list_A = []
for i in A:
    for j in i:
        list_A.append(j)

M_K_ = list(map(int, input().split()))

B = []
for i in range(M_K_[0]):
    B.append(list(map(int, input().split())))

list_B = []
for i in B:
    for j in i:
        list_B.append(j)

print(list_A, list_B)