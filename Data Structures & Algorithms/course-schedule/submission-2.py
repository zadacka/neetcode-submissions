
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's Algorithm
        adjacent = defaultdict(list)
        blocking = {c: 0 for c in range(numCourses)}
        for crs, pre in prerequisites:
            adjacent[crs].append(pre)
            blocking[pre] += 1
            if crs not in blocking:
                blocking[crs] = 0
        
        q = deque([c for c, v in blocking.items() if v == 0])
        finished = 0
        while q:
            course = q.popleft()
            finished += 1
            for affected in adjacent[course]:
                blocking[affected] -= 1
                if blocking[affected] == 0:
                    q.append(affected)
        return finished == numCourses