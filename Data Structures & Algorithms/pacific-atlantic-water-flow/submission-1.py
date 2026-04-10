class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        PACIFIC = set()
        ATLANTIC = set()

        def dfs(r, c, h, ocean):
            if (r,c) in ocean:
                return
            if 0 <= r < ROWS and 0 <= c < COLS and heights[r][c] >= h:
                ocean.add((r, c))
                newheight = heights[r][c]
                dfs(r + 1, c, newheight, ocean)
                dfs(r - 1, c, newheight, ocean)
                dfs(r, c + 1, newheight, ocean)
                dfs(r, c - 1, newheight, ocean) 
        
        pacific_border = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlantic_border = [(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS)]
        for (r, c) in pacific_border:
            dfs(r, c, -1, PACIFIC)
        for (r, c) in atlantic_border:
            dfs(r, c, -1, ATLANTIC)
        return list(PACIFIC.intersection(ATLANTIC))       