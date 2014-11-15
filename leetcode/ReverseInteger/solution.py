# -*- coding:utf-8 -*-
class Solution:
    # @return an integer
    def reverse(self, x):
        num = x
        if x < 0:
            num = -x
        num = int(''.join(list(str(num))[::-1]))
        if num > 2147483647:
            return 0
        if x < 0:
            return -int(num)
        return num
