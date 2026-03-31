class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = f"{n:0b}"
        return sum(1 if c == "1" else 0 for c in bin_str)
        