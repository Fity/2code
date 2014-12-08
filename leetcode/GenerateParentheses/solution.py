# -*- coding:utf-8 -*-
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return []
        ret = []
        self.generate('', n, 0, ret)
        return ret

    def generate(self, s, left, right, ret):
        if left == right == 0:
            ret.append(s)
            return
        if left > 0:
            self.generate(s + '(', left - 1, right + 1, ret)
        if right > 0:
            self.generate(s + ')', left, right - 1, ret)
