# -*- coding:utf-8 -*-
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            t = -x
        else:
            t = x
        y = 0
        while t != 0:
            y = y * 10 + t % 10
            t //= 10
        return x == y
