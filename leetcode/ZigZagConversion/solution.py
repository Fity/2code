# -*- coding:utf-8 -*-
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if not s or nRows <= 1 or len(s) <= nRows:
            return s
        ret = [[] for x in xrange(nRows)]
        step = 1
        row = 0
        for c in s:
            ret[row].append(c)
            if row == 0:
                step = 1
            elif row == nRows - 1:
                step = -1
            row += step
        return ''.join(reduce(lambda x, y: x+y, ret))
