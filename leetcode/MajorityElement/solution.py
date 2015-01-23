# -*- coding:utf-8 -*-
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        c_dict = {}
        for n in num:
            if n in c_dict:
                c_dict[n] += 1
            else:
                c_dict[n] = 1
        size = len(num) // 2
        max_v = 0
        max_n = -1
        for n, v in c_dict.iteritems():
            if v > size and v > max_v:
                max_v = v
                max_n = n
        return max_n

