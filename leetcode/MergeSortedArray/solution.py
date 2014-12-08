# -*- coding:utf-8 -*-
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        la = m - 1
        lb = n - 1
        index = m + n - 1
        while la >= 0 and lb >= 0:
            if A[la] > B[lb]:
                A[index] = A[la]
                la -= 1
            else:
                A[index] = B[lb]
                lb -= 1
            index -= 1
        while lb >= 0:
            A[index] = B[lb]
            lb -= 1
            index -= 1
