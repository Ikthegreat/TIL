Test_case = int(input())

for i in range(Test_case):
    N, K = list(map(int, input().split()))
    Submit = list(map(int, input().split()))
    Student_list = []
    for j in range(1, N+1, 1):
        Student_list.append(j)
    Not_Submit_list = sorted(list(set(Student_list) - set(Submit)))
    Not_Submit = (' '.join(list(map(str, Not_Submit_list))))
    print(f'#{i+1} {Not_Submit}')