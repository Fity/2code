# -*- coding:utf-8 -*-
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if not num:
            return -1
        ret = self.peak(num, 0, len(num))
        if ret is None:
            return -1
        return ret

    def judge(self, num, index):
        length = len(num) - 1
        if index < 0 or index > length:
            return None
        lf = lr = False
        if index == length or num[index] > num[index+1]:
            lr = True
        if index == 0 or num[index] > num[index-1]:
            lf = True
        if lf and lr:
            return index
        else:
            return None

    def peak(self, num, lo, hi):
        if lo >= hi:
            ret = self.judge(num, lo)
            return ret
        mid = (lo + hi) / 2
        middle = self.judge(num, mid)
        if middle is None:
            left = self.peak(num, lo, mid-1)
            right = self.peak(num, mid+1, hi)
            if left is not None:
                return left
            else:
                return right
        return middle
