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
        self.maxValue = -sys.maxint

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = -sys.maxint
        self.maxSum(root)
        return self.maxValue

    def maxSum(self, root):
        if root is None:
            return 0
        lmax = max(0, self.maxSum(root.left))
        rmax = max(0, self.maxSum(root.right))
        self.maxValue = max(self.maxValue, lmax + rmax + root.val)
        return max(lmax, rmax) + root.val



t = TreeNode(2)
t.left = TreeNode(-1)
# t.right = TreeNode(-2)
# t.left.left = TreeNode(-5)
# t.left.left.left = TreeNode(100)
# t.right.right = TreeNode(-4)
s = Solution()
print s.maxPathSum(t)