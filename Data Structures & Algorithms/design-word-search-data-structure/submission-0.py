class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]
        ptr.is_word = True


    def search(self, word: str, entrypoint=None) -> bool:
        ptr = self.root if entrypoint == None else entrypoint
        for idx, char in enumerate(word):
            if char in ptr.children:
                ptr = ptr.children[char]
            elif char == '.':
                rest_of_word = word[idx+1:] if idx < len(word) else "" 
                return any(
                    self.search(c + rest_of_word, ptr) for c in ptr.children
                )

            else:
                return False
        return ptr.is_word