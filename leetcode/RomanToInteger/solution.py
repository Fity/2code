# -*- coding:utf-8 -*-
class Solution:
    # @return an integer
    def romanToInt(self, s):
        convert_map = {'I': 1, 'V': 5, 'X': 10,
                       'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = None
        sum = 0
        end = len(s) - 1
        while end >= 0:
            value = convert_map[s[end]]
            if prev is not None and value < prev:
                sum -= value
            else:
                sum += value
            prev = value
            end -= 1
        return sum
