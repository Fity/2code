# -*- codingLutf-8 -*-
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.stack = []
        self.map = {}
        self.capacity = capacity
        self.size = 0

    # @return an integer
    def get(self, key):
        if key in self.map:
            self.stack.remove(key)
            self.stack.append(key)
            return self.map[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map:
            self.map[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if self.size == self.capacity:
                del self.map[self.stack[0]]
                self.stack.remove(self.stack[0])
                self.stack.append(key)
                self.map[key] = value
            else:
                self.size += 1
                self.map[key] = value
                self.stack.append(key)
