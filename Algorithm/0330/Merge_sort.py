import sys
sys.stdin = open('Merge_sort.txt', 'r')


def m_sort(a):
    global count
    if len(a) <= 1:
        return a
    m = len(a) // 2
    left = []
    right = []
    for x in range(len(a)):
        if x < m:
            left.append(a[x])
        else:
            right.append(a[x])

    left = m_sort(left)
    right = m_sort(right)

    if left[-1] > right[-1]:
        count += 1

    m_ab = []
    l_idx = r_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            m_ab.append(left[l_idx])
            l_idx += 1
        else:
            m_ab.append(right[r_idx])
            r_idx += 1

    m_ab += left[l_idx:] + right[r_idx:]
    return m_ab


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr = m_sort(arr)
    print(f'#{t+1} {arr[len(arr) // 2]} {count}')
