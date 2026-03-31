

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute force
        # result = []
        # for query in queries:
        #     min_length = math.inf
        #     for start, stop in intervals:
        #         if start <= query <= stop:
        #             length = 1 + stop - start
        #             min_length = min(min_length, length)
        #     if min_length == math.inf:
        #         result.append(-1)
        #     else:
        #         result.append(min_length)
        # return result

        # needed some help to get this!
        # slightly tricky ... key points are that we:
        # 1) dynamically build a minheap of length, end 
        # 2) insert into it from queries to get an 'active set'
        # 3) pop from it to clean up invalid entries
        # then 'simples' - the top query is always the min length for the active range!

        from collections import deque
        intervals = deque(sorted(intervals))
        minheap = []
        result = dict()
        for q in sorted(queries):
            while intervals and intervals[0][0] <= q:
                # an interval exists starting before the query!
                start, stop = intervals.popleft()
                length = 1 + stop - start
                heapq.heappush(minheap, (length, stop))

            while minheap and minheap[0][1] < q:
                # the top of the minheap ends before the query
                _ = heapq.heappop(minheap)    
            
            result[q] = minheap[0][0] if minheap else -1
        
        return [result[q] for q in queries]