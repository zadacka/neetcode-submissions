class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        zeros = list()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    zeros.append((r, c))

        def dfs(r:int, c:int, l:list) -> bool:
            if r<0 or r>= ROWS or c<0 or c>= COLS:
                return False
            
            if board[r][c] == 'X' or (r, c) in l:
                return True
            l.append((r, c))
            return dfs(r+1, c, l) and dfs(r-1, c, l) and dfs(r, c+1, l) and dfs(r, c-1, l)
            
        for (r, c) in zeros:
            if board[r][c] == 'O':
                island = list()
                surrounded = dfs(r, c, island )
                if surrounded:
                    for sr, sc in island:
                        board[sr][sc] = 'X'
        