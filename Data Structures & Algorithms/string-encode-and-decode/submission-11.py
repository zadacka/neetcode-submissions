class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + f"{len(word)}.{word}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            word_length, remainder = s.split('.', maxsplit=1)
            word = remainder[:int(word_length)]
            s = remainder[int(word_length):]
            result.append(word)
        return result