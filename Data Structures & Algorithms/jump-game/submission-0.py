class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for idx in reversed(range(len(nums) - 1)):
            jump = nums[idx]
            print(f"idx {idx} and goal {goal}")
            if idx + jump >= goal:
                print('could reach goal!')
                goal = idx
        return goal == 0
            
