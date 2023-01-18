# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

import collections

List = ['eat','tea','tan','ate','nat','bat']

class Solutiuon:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)

        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        return anagram.values()