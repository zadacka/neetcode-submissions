class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.array[self.length]  # zero indexed

    def resize(self) -> None:
        self.capacity *= 2
        self.array.extend([0 for _ in self.array])

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
