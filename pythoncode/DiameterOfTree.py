#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.maxValue = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = 0
        self.maxSum(root)
        return max(self.maxValue - 1, 0)

    def maxSum(self, root):
        if root is None:
            return 0
        lmax = max(0, self.maxSum(root.left))
        rmax = max(0, self.maxSum(root.right))
        self.maxValue = max(self.maxValue, lmax + rmax + 1)
        return max(lmax, rmax) + 1

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

s = Solution()
print s.diameterOfBinaryTree(t)

