class Solution:
    def numIslands_simple_but_slow(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def search(r, c, grid):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = '0'
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
                if grid[r][c] == '1':
                    islands += search(r, c, grid)
        
        return islands

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        untested = set()
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == '1':
                    untested.add((r, c))

        def search(r, c):
            print(f'search starting {r} {c} ... {untested}')
            if (r, c) in untested:
                print(f'removing {r} {c}')
                untested.remove((r, c))
                search(r+1, c)
                search(r-1, c)
                search(r, c+1)
                search(r, c-1)
                return 1
            else:
                return 0
        islands = 0
        while untested:
            (r, c) = list(untested)[0]
            print(f'untested: {untested}')
            print(f'trying {r} {c}')
            islands += 1
            search(r, c)
        return islands