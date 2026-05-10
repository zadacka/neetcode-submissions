class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        treasure_chests = {
            (r, c)
            for r, row in enumerate(grid)
            for c, val in enumerate(row)
            if val == 0
        }

        def dfs(r, c, distance):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            
            if grid[r][c] < distance:
                return
            
            grid[r][c] = distance
            dfs(r+1, c, distance + 1)
            dfs(r-1, c, distance + 1)
            dfs(r, c+1, distance + 1)
            dfs(r, c-1, distance + 1)



        for treasure_chest in treasure_chests:
            r, c = treasure_chest
            dfs(r, c, 0)
        
