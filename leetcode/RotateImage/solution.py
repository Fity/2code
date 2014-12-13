# -*- coding:utf-8 -*-
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n/2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
