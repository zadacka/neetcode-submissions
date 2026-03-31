class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = []
        for s, p in sorted(zip(speed, position), key=lambda x:x[1], reverse=True):
            arrival_time = (target - p) / s
            if not fleets or arrival_time > fleets[-1]:
                fleets.append(arrival_time)
        return len(fleets)