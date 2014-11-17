# -*- coding:utf-8 -*-
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        ret = [1]
        begin = 1
        while rowIndex > 0:
            ret.append(ret[-1] * rowIndex / begin)
            rowIndex -= 1
            begin += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    for x in xrange(5):
        print x, s.getRow(x)
