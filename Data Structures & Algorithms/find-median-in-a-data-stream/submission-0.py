import heapq

class MedianFinder:

    def __init__(self):
        self.left = []  # maxheap
        self.right = [] # minheap
        

    def addNum(self, num: int) -> None:
        if self.left and num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) > len(self.right) + 1:
            n = -heapq.heappop(self.left)
            heapq.heappush(self.right, n)
        
        if len(self.right) > len(self.left) + 1:
            n = heapq.heappop(self.right)
            heapq.heappush(self.left, -n)
        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (self.right[0] + -self.left[0]) / 2 
        