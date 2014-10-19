#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        if root.left is None or root.right is None:
            if root.left == root.right:
                # both are None
                return True
            return False
        return self.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, node1, node2):
        if node1 is None or node2 is None:
            if node1 == node2:
                return True
            return False
        if node1.val != node2.val:
            return False
        return self.isSymmetricRec(node1.left, node2.right) and self.isSymmetricRec(node1.right, node2.left)


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # node = root.left
    # node.left = TreeNode(3)
    # node.right = TreeNode(4)
    # node = root.right
    # node.left = TreeNode(4)
    # node.right = TreeNode(3)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    node = root.left
    node.right = TreeNode(3)
    node = root.right
    node.right = TreeNode(3)

    so = Solution()
    print so.isSymmetric(root)
