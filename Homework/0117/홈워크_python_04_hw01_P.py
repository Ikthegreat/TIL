words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

length = len(words)

used_words = []
used_words.append(words[0])

for i in range(1, length):
    if words[i-1][-1] != words[i][0]:
        print(f'{i+1}번째 사람이 탈락입니다.')
        break
    elif words[i] in used_words:
        print(f'{i+1}번째 사람이 중복 단어로 탈락입니다.')
        break
    else:
        used_words.append(words[i])

# 교수님 방법

# if words[i] in words[:i]:
#     print(f'{i}번째 사람이 중복 단어로 탈락입니다.')
#     break