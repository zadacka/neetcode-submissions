from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache=defaultdict(list)        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f"set called with {key}: {value} timestamp {timestamp}")
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print(f"get called with {key}, timestamp {timestamp}")
        time_val_tuple = self.cache[key]
        for time, val in reversed(time_val_tuple):
            if timestamp >= time:
                return val
        return ""