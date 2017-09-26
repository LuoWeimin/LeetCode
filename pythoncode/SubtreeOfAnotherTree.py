#!/usr/bin/python
# -*- coding: UTF-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traverse(s, t)

    def equals(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)

    def traverse(self, s, t):
        return s is not None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))

s = Solution()
tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
test = TreeNode(2)
test.left = TreeNode(5)
test.right = TreeNode(6)
print s.isSubtree(tree, test)
