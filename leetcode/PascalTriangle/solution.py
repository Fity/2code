# -*- coding:utf-8 -*-
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ret = []
        if numRows == 0:
            return []
        if numRows == 1:
            ret.append([1])
            return ret
        if numRows == 2:
            ret.extend([[1], [1,1]])
            return ret
        ret.extend([[1], [1,1]])
        prev = [1,1]
        for x in xrange(numRows - 2):
            row = [1]
            row_prev = prev[0]
            for v in prev[1:]:
                row.append(row_prev + v)
                row_prev = v
            row.append(1)
            prev = row
            ret.append(row)
        return ret
