from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """ This requires a bit of thinking... (I looked at the solution)"""
        counter = Counter(tasks)                # let's use a Counter
        char, maxf = counter.most_common(1)[0]  # find which letter is most common  
        idle = (maxf - 1) * n                   # A _ _ A _ _ A <- max idle would be (maxf - 1) * n
        del counter[char]                       # remove this from the Counter so we can...
        for char, count in counter.items():     # look at each other task and try to fit it into gaps
            idle -= min(count, maxf-1)          # you can fill up to maxf-1 idle slots (likely less)
        return len(tasks) + max(idle, 0)        # you need at least len(tasks) cycles