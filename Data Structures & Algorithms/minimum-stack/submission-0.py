class MinStack:

    def __init__(self):
        self.m = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.m:
            if val < self.m[-1]:
                self.m.append(val)
            else:
                self.m.append(self.m[-1])
        else:
            self.m.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]
