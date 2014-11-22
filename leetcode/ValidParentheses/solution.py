# -*- coding:utf-8 -*-
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        pair = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif stack and pair[stack[-1]] == c:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
