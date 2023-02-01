Test_case = int(input())

for i in range(Test_case):
    N, K = list(map(int, input().split()))
    Score = list(map(int, input().split()))

    Top_Score = sorted(Score)[-K:]
    Answer = sum(Top_Score)

    print(f'#{i+1} {Answer}')