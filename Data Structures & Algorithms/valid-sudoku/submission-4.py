class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqrs = defaultdict(set)

        for row, line in enumerate(board):
            for col, value in enumerate(line):
                if value == '.':
                    continue
                square = (row // 3, col // 3)
                if value in cols[col]: 
                    print(f"{value} already in col {col}")
                    return False
                if value in rows[row]: 
                    print(f"{value} already in row {row}")
                    return False
                if value in sqrs[square]: 
                    print(f"{value} already in square {square}")
                    print(sqrs)
                    return False
                cols[col].add(value)
                rows[row].add(value)
                sqrs[square].add(value)
        return True
