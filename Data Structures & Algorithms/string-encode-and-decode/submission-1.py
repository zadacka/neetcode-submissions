class Solution:

    def encode1(self, strs: List[str]) -> str:
        break_positions = [0]
        for s in strs:
            break_positions.append(break_positions[-1] + len(s))
        break_positions = ','.join([str(b) for b in break_positions])
        result = f"{len(break_positions)},{break_positions}{''.join(strs)}"
        print(result)
        return result

    def decode1(self, s: str) -> List[str]:
        len_break_positions = s.split(',', maxsplit=1)[0]
        p1 = len(len_break_positions) + 1
        p2 = p1 + int(len_break_positions)

        breaks = s[p1:p2]
        breaks = [int(b) for b in breaks.split(',')]
        print(f"breaks: {breaks}")
        print(f"remainder: {s[p2:]}")

        str_to_split = s[p2:]
        result = []
        p = 0
        for b in breaks[1:]:
            result.append(str_to_split[p:b])
            p = b
        return result

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            list_s = s.split('#', maxsplit=1)
            c, s = int(list_s[0]), list_s[1]
            word, s = s[:c], s[c:]
            result.append(word)
        return result
