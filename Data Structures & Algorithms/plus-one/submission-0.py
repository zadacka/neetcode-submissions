class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = True
        for d in reversed(digits):
            if carry:
                d += 1
            if d == 10:
                d = 0
                carry = True
            else:
                carry = False
            result.append(d)
        if carry:
            result += [1]

        return result[::-1]
        