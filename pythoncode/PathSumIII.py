#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        return self.calSubTree(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def calSubTree(self, node, pre, sum):
        if node is None:
            return 0
        cur = pre + node.val
        if cur == sum:
            count = 1
        else:
            count = 0
        return count + self.calSubTree(node.left, cur, sum) + self.calSubTree(node.right, cur, sum)



s = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(3)
tree.right.right = TreeNode(2)
print s.pathSum(tree, 3)