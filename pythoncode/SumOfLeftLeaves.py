# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0
        elif root.left is None:
            return self.rightTree(root.right)
        elif root.right is None:
            return self.leftTree(root.left)
        else:
            return self.leftTree(root.left) + self.rightTree(root.right)

    def leftTree(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val
        elif node.left is None:
            return self.rightTree(node.right)
        elif node.right is None:
            return self.leftTree(node.left)
        else:
            return self.leftTree(node.left) + self.rightTree(node.right)

    def rightTree(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        elif node.left is None:
            return self.rightTree(node.right)
        elif node.right is None:
            return self.leftTree(node.left)
        else:
            return self.leftTree(node.left) + self.rightTree(node.right)


t = TreeNode(3)
t.left = TreeNode(9)
t.left.left = TreeNode(1)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print s.sumOfLeftLeaves(t)
