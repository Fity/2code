# -*- coding:utf-8 -*-
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return 0
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        if target > A[lo]:
            return lo + 1
        else:
            return lo
