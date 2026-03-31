class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_ends_here = False

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word_ends_here = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = TrieNode()
        for word in words:
            t.add_word(word)
        
        b = dict()
        for r, line in enumerate(board):
            for c, char in enumerate(line):
                b[(r, c)] = char
        
        valid, seen = set(), set()
        
        def dfs(r, c, node, word):
            char = b.get((r, c), None)
            if (r, c) in seen or char not in node.children:
                return
            seen.add((r, c))
            node = node.children[char]
            word += char
            if node.word_ends_here:
                valid.add(word)
            # this is repetitive but actually quite simple/clean
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            # fix seen when we recurse back up
            seen.remove((r, c))

        for (r, c) in b:
            dfs(r, c, t, "")

        return list(valid)