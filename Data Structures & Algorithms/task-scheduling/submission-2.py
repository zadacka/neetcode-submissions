class Solution:
    def leastInterval_math(self, tasks: List[str], n: int) -> int:    
        from collections import Counter    
        frequency = sorted(v for v in Counter(tasks).values())
        maxf = max(frequency)
        end = sum([1 if f == maxf else 0 for f in frequency])
        time = (maxf - 1) * (n + 1) + end
        return max(len(tasks), time)

    def leastInterval(self, tasks: List[str], n: int) -> int:    
        import heapq
        from collections import deque, Counter
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while maxheap or q:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxheap) # maxheap has -ves 
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time