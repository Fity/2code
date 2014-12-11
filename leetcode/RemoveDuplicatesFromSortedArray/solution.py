# -*- coding:utf-8 -*-
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        length = len(A)
        ret = index = 1
        while index < length:
            if A[index] != A[ret - 1]:
                A[ret] = A[index]
                ret += 1
            index += 1
        return ret
