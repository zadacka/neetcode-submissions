class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rc2char = dict()
        for r, line in enumerate(board):
            for c, char in enumerate(line):
                rc2char[(r,c)] = char

        def word_exists(r, c, word, seen):
            if word == "": 
                return True
            if (r,c) in seen or (r,c) not in rc2char:
                return False
            if word[0] != rc2char[(r,c)]:
                return False
            
            new_seen = seen | {(r, c)}
            return any([
                    word_exists(r+1, c, word[1:], new_seen),
                    word_exists(r-1, c, word[1:], new_seen),
                    word_exists(r, c+1, word[1:], new_seen),
                    word_exists(r, c-1, word[1:], new_seen),
            ])
            

        for (r,c), char in rc2char.items():
            if word_exists(r, c, word, set()):
                return True
        return False            