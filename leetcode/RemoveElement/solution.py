# -*- coding:utf-8 -*-
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        lens = len(A)
        while True:
            try:
                A.remove(elem)
            except:
                return lens
            else:
                lens -= 1
