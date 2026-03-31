from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        char, maxf = counter.most_common(1)[0]
        idle = (maxf - 1) * n
        del counter[char]
        for char, count in counter.items():
            idle -= min(count, maxf-1)
        return len(tasks) + max(idle, 0)