class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = [] # nice: min @ each stack pos
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = min(self.mins[-1], val) if self.mins else val
        self.mins.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
