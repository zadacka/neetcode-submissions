class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair index, height
        max_rectangle = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                rectangle = h * (idx - i)
                max_rectangle = max(max_rectangle, rectangle)
                start = i
            stack.append((start, height))
        
        for i, h in stack:
            rectangle = h * (len(heights) - i)
            max_rectangle = max(max_rectangle, rectangle)
        return max_rectangle

