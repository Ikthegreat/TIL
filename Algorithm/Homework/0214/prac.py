a = int(input())
n = int(input())

i = 0
lst = [1]
while i < n:
    lst.append((a*10)+a)
    a = (a*10)+a
    i +=1
for j in lst:
    print(j)