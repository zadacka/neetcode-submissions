class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # thought process:
        # Counter (hash map of task to count)
        # Frequency (map of occurrence to tasks(s))
        if n == 0:
            return len(tasks)
        
        from collections import Counter
        c = Counter(tasks)
        frequency = sorted(v for v in c.values())
        maxf = max(frequency)
        end = sum([1 if f == maxf else 0 for f in frequency])
        time = (maxf - 1) * (n + 1) + end
        return max(len(tasks), time)
        # Starting with the most frequent, run through the instructions in threes
        # Place the first, second, third most frequent instructions
        # ... use Nulls if any run out
        # Decrement the counters
        # Continue

        # (Max heap, pop the top three ... update them ... push them if nonzero)
        