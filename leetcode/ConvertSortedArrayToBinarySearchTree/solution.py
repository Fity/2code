# -*- coding:utf-8 -*-
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        lo = 0
        hi = len(num) - 1
        mid = (lo + hi) // 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[lo:mid])
        root.right = self.sortedArrayToBST(num[mid+1:hi+1])
        return root
