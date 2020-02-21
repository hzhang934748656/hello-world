class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if self.min_stack[-1] < x:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(x)
        self.stack.append(x)
    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
