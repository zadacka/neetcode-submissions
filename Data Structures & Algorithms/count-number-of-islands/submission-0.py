class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def search(r, c, grid):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = 0
                search(r+1, c, grid)
                search(r-1, c, grid)
                search(r, c+1, grid)
                search(r, c-1, grid)
                return 1
            else:
                return 0
        islands = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                islands += search(r, c, grid)
        
        return islands
