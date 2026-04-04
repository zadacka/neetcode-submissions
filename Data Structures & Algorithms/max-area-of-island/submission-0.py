class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ones = {
            (r, c)
            for r, row in enumerate(grid)
            for c, val in enumerate(row)
            if val == 1
        }

        def dfs(r, c):
            if (r, c) in ones:
                ones.remove((r, c))
                island_size = 1
                island_size += dfs(r+1, c)
                island_size += dfs(r-1, c)
                island_size += dfs(r, c+1)
                island_size += dfs(r, c-1)
                return island_size
            else:
                return 0

        max_island = 0
        while ones:
            (r, c) = next(iter(ones))
            size = dfs(r, c)
            max_island = max(size, max_island)
        return max_island