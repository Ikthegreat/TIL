n = int(input())

n_int = int(n)

n_lst = list(str(n))

def fn_d(n):
    num = 0
    for i in range(0, len(n_lst)):
        num = num + int(n_lst[i])
    return num + n

fn_d(n)

if fn_d(n) == 

print(fn_d(n))