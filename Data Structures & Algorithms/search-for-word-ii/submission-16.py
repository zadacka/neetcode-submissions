class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_ends_here = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word_ends_here = True

    def search_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word_ends_here
    
    def search_prefix(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wd = WordDictionary()
        for word in words:
            wd.add_word(word)
        
        b = dict()
        for r, line in enumerate(board):
            for c, char in enumerate(line):
                b[(r, c)] = char
        
        valid_words = set()
        
        def search(rc, word_so_far, seen):
            if not wd.search_prefix(word_so_far):
                return 
            
            if wd.search_word(word_so_far):
                nonlocal valid_words
                valid_words.add(word_so_far)
            row, col = rc
            next_positions = {(row + 1, col), (row - 1, col), (row, col + 1), (row, col -1)}
            next_positions = next_positions & b.keys() - seen
            # print(word_so_far, f"current position {rc} so next positions ... {next_positions} as seen {seen}")
            for next_position in next_positions:
                next_letter = b[next_position]
                search(next_position, word_so_far + next_letter, seen | set([next_position]))
                

        
        for (rowcol), first_char in b.items():
            seen = set([rowcol])
            word = first_char
            search(rowcol, word, seen)
        return list(valid_words)
                



                