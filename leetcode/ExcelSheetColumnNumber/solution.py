# -*- coding:utf-8 -*-
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        col = 0
        for c in s:
            col = col * 26 + ord(c) - ord('A') + 1
        return col
