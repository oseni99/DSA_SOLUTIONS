class MinStack:

    def __init__(self):
        self.push_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.push_stack.append(val)
        x = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(x)

    def pop(self) -> None:
        self.min_stack.pop()
        self.push_stack.pop()

    def top(self) -> int:
        return self.push_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()