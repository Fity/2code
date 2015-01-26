# -*- coding:utf-8 -*-
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        sum_list = []
        self._sumNumbers(root, 0, sum_list)
        return sum(sum_list)

    def _sumNumbers(self, root, s, sum_list):
        if root is None:
            return

        s = s * 10 + root.val
        if root.left is None and root.right is None:
            sum_list.append(s)
            return

        self._sumNumbers(root.left, s, sum_list)
        self._sumNumbers(root.right, s, sum_list)
