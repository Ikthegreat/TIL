score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90 # algorithm 점수 추가
score['python'] = 85 # python 점수 수정

sumscore = sum(score.values()) # sumscore 는 과목 총 점수
average = sumscore / len(score) # average 는 총 점수 나누기 과목의 수

print(average)