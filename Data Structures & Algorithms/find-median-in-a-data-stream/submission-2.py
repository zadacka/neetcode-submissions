class MedianFinder:

    def __init__(self):
        self.lower_half = []  # max heap
        self.upper_half = []  # min heap

    def addNum(self, num: int) -> None:
        if self.upper_half and num > self.upper_half[0]:
            heapq.heappush(self.upper_half, num)
        else:
            heapq.heappush_max(self.lower_half, num)

        # if we have become unbalanced, redistribute from lower to upper
        if len(self.lower_half) == len(self.upper_half) + 2:
            popped = heapq.heappop_max(self.lower_half)
            heapq.heappush(self.upper_half, popped)
        if len(self.upper_half) == len(self.lower_half) + 2:
            popped = heapq.heappop(self.upper_half)
            heapq.heappush_max(self.lower_half, popped)

        print(self.lower_half, self.upper_half)

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return self.lower_half[0]
        elif len(self.lower_half) < len(self.upper_half):
            return self.upper_half[0]
        else:
            return (self.lower_half[0] + self.upper_half[0]) / 2
        