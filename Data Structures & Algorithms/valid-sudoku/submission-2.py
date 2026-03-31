def has_duplicates(iterable):
    seen = set()
    for i in iterable:
        if i != '.' and i in seen:
            return True
        seen.add(i)
    return False

def get_sqs(board):
    from collections import defaultdict
    result = defaultdict(list)
    for c, row in enumerate(board):
        for r, num in enumerate(row):
            print(f"{r},{c} ->  {r//3}, {c//3} for {num}")
            result[(r // 3, c // 3)].append(num)
    return list(result.values())

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if any(has_duplicates(row) for row in board):
            for row in board:
                if has_duplicates(row):
                    print(f"duplicate in row {row}")
            return False

        if any(has_duplicates(col) for col in zip(*board)):
            for col in zip(*board):
                if has_duplicates(col):
                    print(f"duplicate in col {col}")
            return False

        if any(has_duplicates(sq) for sq in get_sqs(board)):
            for sq in get_sqs(board):
                if has_duplicates(sq):
                    print(f"duplicate in sq {sq}")
            return False

        return True