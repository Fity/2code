# -*- coding:utf-8 -*-
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            neg_flag = True
            n = -n
        else:
            neg_flag = False
        ret = 1
        while n > 0:
            if n % 2 == 1:
                ret *= x
            x = x * x
            n //= 2
        if neg_flag:
            return 1 / ret
        return ret
