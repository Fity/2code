# -*- coding:utf-8 -*-
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a = b = 1
        n = n - 1
        while n > 0:
            tmp = a
            a = a + b
            b = tmp
            n -= 1
        return a
