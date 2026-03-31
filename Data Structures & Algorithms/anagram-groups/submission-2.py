def frequencycount(word):
    result = [0] * 26
    for char in word:
        idx = ord(char) - ord('a')
        result[idx] += 1
    return tuple(result)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for word in strs:
            key = frequencycount(word)
            anagrams[key].append(word)
        return [v for v in anagrams.values()]