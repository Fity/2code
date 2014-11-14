# -*- coding:utf-8 -*-
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if not self.stack:
            return None
        if self.min_stack and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    # @return an integer
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if not self.stack:
            return None
        return self.min_stack[-1]
