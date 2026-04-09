class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh_oranges = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh_oranges > 0:
            oranges_to_process_this_cycle = len(q)
            for _ in range(oranges_to_process_this_cycle):
                r, c = q.popleft()
                for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh_oranges -= 1
            time += 1
        return -1 if fresh_oranges else time