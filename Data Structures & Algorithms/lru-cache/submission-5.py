class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
            self.cache[key] = value
