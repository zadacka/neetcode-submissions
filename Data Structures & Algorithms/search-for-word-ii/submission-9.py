class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        ptr = self
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]
        ptr.is_word = True


class Solution:
    # used the neetcode solution here - some REALLY nice tricks used ...
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word) # build your trie on the input words (small) not all grid permuations (huge)

        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or board[r][c] not in node.children
            ):
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                result.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)     
            visited.remove((r, c))  # add then remove the visited list after the dfs dive! 

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")  # closure over the result output, no accumulation

        return list(result)