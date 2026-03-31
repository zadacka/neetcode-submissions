
def get_sub_box(board):
    result = []
    for row_offset in range(0,7,3):
        for col_offset in range(0,7,3):
            result.append(
                board[0+row_offset][0+col_offset:3+col_offset] + 
                board[1+row_offset][0+col_offset:3+col_offset] + 
                board[2+row_offset][0+col_offset:3+col_offset],
            )
    return result

def contains_duplicate(iterable):
    space_stripped = [x for x in iterable if x != '.']
    if not space_stripped:
        return False  # empty board is 'okay'
    return Counter(space_stripped).most_common(1)[0][1] > 1

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}        
        from collections import Counter
        for row in board:
            if contains_duplicate(row):
                print(f"duplicate in row: {row}")
                return False
        
        for column in zip(*board):
            if contains_duplicate(column):
                print(f"duplicate in column: {column}")
                return False
        
        for sub_box in get_sub_box(board):
            if contains_duplicate(sub_box):
                print(f"duplicate in sub_box: {sub_box}")
                return False
        
        return True