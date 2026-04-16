class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def mark_safe(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                board[r][c] = 'S'
                mark_safe(r-1, c)
                mark_safe(r+1, c)
                mark_safe(r, c+1)
                mark_safe(r, c-1)
        
        for r in range(ROWS):
            mark_safe(r, 0)
            mark_safe(r, COLS-1)
        
        for c in range(COLS):
            mark_safe(0, c)
            mark_safe(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O' 