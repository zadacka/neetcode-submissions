class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dd = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            dd[sorted_string].append(s)
        return [l for l in dd.values()]