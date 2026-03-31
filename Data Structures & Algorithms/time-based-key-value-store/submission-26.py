from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # {key: [(time, value), ] }
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append( (timestamp, value) )

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value_history = self.map.get(key, [])
        l, r = 0, len(value_history) - 1
        while l <= r:
            m = (l + r) // 2
            if value_history[m][0] <= timestamp:
                result = value_history[m][1]
                l = m + 1
            else:
                r = m - 1
        return result