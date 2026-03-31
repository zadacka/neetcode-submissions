class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(idx:int, curr:list, total:int) -> None:
            print(idx, curr, total)
            if total == target:
                result.append(curr.copy())
                return
            if total > target or idx == len(candidates):
                return
            
            # try adding the value at idx
            curr.append(candidates[idx])
            dfs(idx+1, curr, total + candidates[idx])

            # adding idx didn't work so pop it and skip ahead to the first different value 
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, curr, total)
        dfs(0, [], 0)
        return list(list(r) for r in result)