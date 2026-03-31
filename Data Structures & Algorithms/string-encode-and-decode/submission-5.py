class Solution:

    def _encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str_string = ""
        str_lengths = []

        for s in strs:
            str_string += s
            str_lengths.append(len(s))

        str_lengths_str = ','.join([str(s) for s in str_lengths])
        str_lengths_str_length = len(str_lengths_str)
        return f"{str_lengths_str_length},{str_lengths_str}{str_string}"

    def _decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        split_length, *other = s.split(',')
        split_length = int(split_length)
        other = ','.join(other)
        lengths = other[:split_length]
        lengths = [int(l) for l in lengths.split(',')]
        str_to_split = other[split_length:]
        result = []
        start = 0
        for length in lengths:
            result.append(str_to_split[start:start+int(length)])
            start += int(length)
        return result

    def encode(self, strs):
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s):
        result = []
        while s:
            c, s = s.split('#', maxsplit=1)  # we can always split by the first '#'
            word, s = s[:int(c)], s[int(c):]
            result.append(word)
        return result