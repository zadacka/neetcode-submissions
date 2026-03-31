class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        bit = 0
        while n:
            val = (2**bit)
            a = n ^ val # xor it
            if a < n:
                # there must have been a 1 there for it to get smaller
                result += 1
                n = a
            bit += 1
        return result




        bin_str = f"{n:0b}"
        return sum(1 if c == "1" else 0 for c in bin_str)
        