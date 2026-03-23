# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def similar(p, q):
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False

            return similar(p.left, q.left) and similar(p.right, q.right)

        return similar(p, q)