Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    nums = list(map(int, input().split()))
    # [1] 최소힙에 데이터를 저장
    heap = [0] * (N + 1)
    last = 0
    for n in nums:
        last += 1
        heap[last] = n
        # 부모 노드가 있고, 나보다 크면 교환
        c = last
        while 0 < c//2 and heap[c//2] > heap[c]:
            heap[c//2], heap[c] = heap[c], heap[c//2]
            c = c//2

    # last 의 조상 노드들의 값의 합을 저장
    result = 0
    c = last//2
    while c > 0:          # 존재하는 조상인 경우
        result += heap[c]
        c //= 2           # 기준점을 부모 노드로 이동

    print(f'#{t+1} {result}')