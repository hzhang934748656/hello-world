class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.top_item = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.top_item = x
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        temp_list = []
        while len(self.q)>1:
            self.top_item= self.q.pop(0)
            temp_list.append(self.top_item)
        pop_item = self.q.pop(0)
        self.q = temp_list
        return pop_item
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_item

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) ==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
