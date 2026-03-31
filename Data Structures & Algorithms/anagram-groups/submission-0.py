class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            anagrams[key].append(s)
        return [values for values in anagrams.values()]
