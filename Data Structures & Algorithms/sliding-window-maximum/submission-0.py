class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        window = deque(nums[0:k], maxlen=k)
        max_vals = [max(window)]
        for num in nums[k:]:
            window.append(num)
            max_vals.append(max(window))
        return max_vals
            
        