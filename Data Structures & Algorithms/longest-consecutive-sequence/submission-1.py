class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        this_streak = 0
        previous = None
        
        counts = collections.Counter(nums)
        for num in sorted(counts):
            if previous is None or num == previous + 1:
                this_streak += 1
            else:
                max_streak = max(this_streak, max_streak)
                this_streak = 1
            previous = num
        # print(f"this_streak {this_streak}, max_streak {max_streak}")
        max_streak = max(this_streak, max_streak)
        return max_streak


        