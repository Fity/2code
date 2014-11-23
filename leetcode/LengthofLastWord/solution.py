# -*- coding:utf-8 -*-
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        w_list = filter(None, s.split())
        if not w_list:
            return 0
        return len(w_list[-1])

