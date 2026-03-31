class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqrs = defaultdict(set)

        for r, row in enumerate(board):
            for c, num in enumerate(row):
                if num == '.': continue
                if num in cols[c]: return False
                if num in rows[r]: return False
                if num in sqrs[(r//3, c//3)]: return False
                cols[c].add(num)
                rows[r].add(num)
                sqrs[(r//3, c//3)].add(num)
        return True