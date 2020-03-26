"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) Push element x onto stack.
pop() Removes the element on top of the stack.
top() Get the top element.
getMin() Retrieve the minimum element in the stack.


all the operations have to be constant time operations.

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minNum = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minNum:
            if x <= self.minNum[-1]:  # x is smaller than current minNum
                self.minNum.append(x)
        else:
            self.minNum.append(x)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minNum[-1]:
                self.minNum = self.minNum[:-1]
                self.stack = self.stack[:-1]
            else:
                self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.minNum:
            return self.minNum[-1]
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minstack = MinStack()

minstack.pop()
minstack.push(10)
minstack.push(9)
print(minstack.getMin())
minstack.push(8)
print(minstack.getMin())
minstack.push(7)
print(minstack.getMin())
minstack.push(6)
print(minstack.getMin())
minstack.pop()
print(minstack.getMin())
print(minstack.stack)
print(minstack.getMin())
minstack.pop()
print(minstack.stack)


