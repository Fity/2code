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
    def maxDepth(self, root):
        if not root:
            return 0
        hight = max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 1 + hight
