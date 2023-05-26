#  id 만 불러오기

#


lst1 = ['killer', 'horror', 'dream', 'power']
lst2 = ['killer', 'power', 'drea', 'horro']
intersection1 = list(set(lst1) & set(lst2))
print(intersection1)
intersection2 = list(set(lst1).intersection(lst2))
print(intersection2)

similarity = (len(intersection2) / len(lst2))

recommend_movie = []

if similarity >= 0.5:
    recommend_movie.append((movie_id, similarity))