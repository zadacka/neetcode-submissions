class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_ends_here = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()


    def addWord(self, word: str) -> None:
        node = self.node
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_ends_here = True

    def search(self, word: str) -> bool:
        # note - this isn't as good as it should be, as we're re-searching the prefix 
        # it would be better to implement a dfs method (like in the solution) which can start the
        # other searches from the node we are at when the '.' branch-out happens
        node = self.node
        for char in word:
            if char == '.':
                replacements = [word.replace('.', k, count=1) for k in node.children.keys()]
                return any(self.search(r) for r in replacements )
            elif char not in node.children:
                return False
            else:
                node = node.children[char]
        return node.word_ends_here