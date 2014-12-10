# -*- coding:utf-8 -*-
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        ret = []
        if root:
            self.traversal(root, ret)
        return ret

    def traversal(self, root, ret):
        if root is None:
            return
        ret.append(root.val)
        self.traversal(root.left, ret)
        self.traversal(root.right, ret)
