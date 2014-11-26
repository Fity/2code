# -*- coding:utf-8 -*-
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits

    def plusOne(self, digits):
        length = len(digits) - 1
        pre = 0
        digits[length] += 1
        while length >= 0:
            c = digits[length] + pre
            digits[length] = c % 10
            pre = c // 10
            length -= 1
        if pre:
            return [1] + digits
        return digits
