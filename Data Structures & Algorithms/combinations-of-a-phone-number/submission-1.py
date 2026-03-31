class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "0": "+",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits: return []
        result = [char for char in mapping[digits[0]]]
        print(f"starting: {result}")
        for digit in digits[1:]:
            new_result = []
            for r in result:
                for next_digit in mapping[digit]:
                    new_result.append( r + next_digit)
            result = new_result
        return result

