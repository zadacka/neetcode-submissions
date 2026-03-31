class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def dfs(idx:int, curr:list, total:int) -> None:
            print(idx, curr, total)
            if total == target:
                result.add(tuple(sorted(curr)))
                return
            if total > target or idx == len(candidates):
                return
            
            curr.append(candidates[idx])
            dfs(idx+1, curr, total + candidates[idx])

            curr.pop()
            dfs(idx+1, curr, total)
        dfs(0, [], 0)
        return list(list(r) for r in result)