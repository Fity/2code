# -*- coding:utf-8 -*-
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        h = len(num) - 1
        while l < h:
            mid = (l + h) // 2
            if num[l] > num[mid]:
                h = mid
            elif num[h] < num[mid]:
                l = mid + 1
            else:
                break
        return num[l]
