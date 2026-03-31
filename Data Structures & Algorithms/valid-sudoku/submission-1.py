

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # keys = ( r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue
                if (char in cols[c] or char in rows[r] or char in squares[(r//3, c//3)]):
                    return False
                cols[c].add(char)
                rows[r].add(char)
                squares[(r//3, c//3)].add(char)
        return True