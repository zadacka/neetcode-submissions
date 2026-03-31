class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:    
        from collections import Counter
        
        frequency = sorted(v for v in Counter(tasks).values())
        maxf = max(frequency)
        end = sum([1 if f == maxf else 0 for f in frequency])
        time = (maxf - 1) * (n + 1) + end
        return max(len(tasks), time)
