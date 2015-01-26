# -*- coding:utf-8 -*-
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        idx_a = len(a) - 1
        idx_b = len(b) - 1
        bsum = []
        overflow = False
        while idx_a >= 0 or idx_b >= 0:
            if idx_a < 0:
                ba = '0'
            else:
                ba = a[idx_a]
            if idx_b < 0:
                bb = '0'
            else:
                bb = b[idx_b]
            if overflow:
                ret = '1'
            else:
                ret = '0'
            overflow = False
            if ba == bb:
                if ba == '1':
                    overflow = True
            elif ret == '1':
                ret = '0'
                overflow = True
            else:
                ret = '1'
            bsum.append(ret)
            idx_a -= 1
            idx_b -= 1
        if overflow:
            bsum.append('1')
        return ''.join(bsum[::-1])
