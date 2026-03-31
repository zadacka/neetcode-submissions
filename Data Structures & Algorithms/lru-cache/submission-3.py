class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = dict()
        

    def get(self, key: int) -> int:
        if key in self.store:
            value = self.store[key]
            del self.store[key]
            self.store[key] = value

        return self.store.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            del self.store[key]
        self.store[key] = value

        if len(self.store) > self.capacity:
            oldest_key = list(self.store.keys())[0]
            print(f"{self.store} is more than {self.capacity} so evicting {oldest_key}")
            del self.store[oldest_key]
