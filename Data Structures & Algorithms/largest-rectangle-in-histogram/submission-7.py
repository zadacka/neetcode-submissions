class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best =  0      # max rectangle seen
        stack = []     # idx, height
        for idx, height in enumerate(heights):
            
            while stack and height < stack[-1][1]:
                stack_idx, stack_height = stack.pop()
                area = stack_height * (idx - stack_idx)
                best = max(best, area)
                if not stack or stack[-1][1] < height:
                    stack.append((stack_idx, height))  # reset max height for previous popped start to this
            

            if stack and height == stack[-1][1]:
                pass
            else:
                stack.append((idx, height))
            print(best, stack)
        
        idx += 1
        while stack:
            stack_idx, stack_height = stack.pop()
            area = stack_height * (idx - stack_idx)
            best = max(best, area)            
        return best
