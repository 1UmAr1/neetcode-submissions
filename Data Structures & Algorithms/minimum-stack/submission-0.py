class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_value stack if empty or if current val is smaller or equal
        if not self.min_value or val <= self.min_value[-1]:
            self.min_value.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_value[-1]:
            self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]