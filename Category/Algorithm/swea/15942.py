Test_case = int(input())

for t in range(Test_case):
    n, k = list(map(int, input().split()))
    planet = list(map(int, input().split()))
    planet.sort()
    for i in range(len(planet), 0, -1):
        ufo = k
        if i <= ufo:
            ufo