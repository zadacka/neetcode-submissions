
class Node:
    def __init__(self, word_ends_here=False):
        self.word_ends_here = word_ends_here
        self.map = dict()


class PrefixTree:

    def __init__(self):
        self.trie = Node()
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr.map:
                curr.map[char] = Node()
            curr = curr.map[char]
        curr.word_ends_here = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr.map:
                return False
            curr = curr.map[char]
        return curr.word_ends_here
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr.map:
                return False
            curr = curr.map[char]
        return True
        