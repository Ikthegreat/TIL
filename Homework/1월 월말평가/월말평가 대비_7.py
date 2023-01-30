def get_strong_word(word1, word2):

    result1 = 0
    for char1 in word1:
        result1 += ord(char1)

    result2 = 0
    for char2 in word2:
        result2 += ord(char2)

    if result1 < result2:
        return word1
    elif result1 < result2:
        return word2
    elif result1 == result2:
        