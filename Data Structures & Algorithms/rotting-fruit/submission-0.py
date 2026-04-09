class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        import copy
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        while True:
            print(grid)
            rotting = [
                (r, c)
                for r, row in enumerate(grid)
                for c, val in enumerate(row)
                if val == 2
            ]

            something_rotted = False
            for (r, c) in rotting:
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        something_rotted = True
                grid[r][c] = 3  # don't try this one again

            if not something_rotted:
                break

            minutes += 1

        for row in grid:
            if any(
                val == 1 
                for row in grid 
                for val in row
            ):
                return -1
        return minutes