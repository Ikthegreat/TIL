import sys
sys.stdin = open('Quick_sort.txt', 'r')


def qsort(ls):
    # 종료 조건
    if len(ls) <= 1:  # 길이가 1 보다 작다면, 정렬 끝
        return ls
    # 단위 작업 : pivot 기준으로 양쪽 정렬
    pivot = ls.pop()
    left = []
    right = []
    for n in ls:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    # 좌 + pivot + 우 정렬 결과 리턴
    return qsort(left) + [pivot] + qsort(right)


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = qsort(arr)
    print(f'#{t+1} {arr[N // 2]}')
