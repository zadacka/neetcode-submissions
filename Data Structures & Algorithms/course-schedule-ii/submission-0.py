class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Khan's Algorithm 
        # recording the 'completed' courses

        block_count = [0 for _ in range(numCourses)]
        blocked = defaultdict(list)

        for crs, pre in prerequisites:
            block_count[crs] += 1
            blocked[pre].append(crs)
        
        result = []
        q = deque([c for c in range(numCourses) if block_count[c] == 0])
        while q:
            crs = q.popleft()
            result.append(crs)
            for c in blocked[crs]:
                block_count[c] -= 1
                if block_count[c] == 0:
                    q.append(c)
        if len(result) == numCourses:
            return result
        else:
            return []