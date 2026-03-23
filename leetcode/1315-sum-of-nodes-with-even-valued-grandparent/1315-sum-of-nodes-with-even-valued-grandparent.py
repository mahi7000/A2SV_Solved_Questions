# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def summ(root):
            if not root:
                return 0

            x = 0
            if root and (root.left or root.right) and (root.val % 2 == 0):
                if root.left:
                    x += root.left.left.val if root.left.left else 0
                    x += root.left.right.val if root.left.right else 0
                if root.right:
                    x += root.right.left.val if root.right.left else 0
                    x += root.right.right.val if root.right.right else 0

            return x + summ(root.left) + summ(root.right)

        return summ(root)