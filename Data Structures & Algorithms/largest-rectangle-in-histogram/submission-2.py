class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair index, height
        max_rectangle = 0

        for idx, height in enumerate(heights):
            i = idx
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                rectangle = h * (idx - i)
                print(f"starting {i} and ending {idx} with area {rectangle}")
                max_rectangle = max(max_rectangle, rectangle)
            stack.append((min(i, idx), height))
        
        idx = len(heights)
        while stack:
            i, h = stack.pop()
            rectangle = h * (idx - i)
            print(f"starting {i} and ending {idx} with area {rectangle}")
            max_rectangle = max(max_rectangle, rectangle)
        return max_rectangle

