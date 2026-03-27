# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.summ = 0
        def distribute(node):
            if not node:
                return 0

            left = distribute(node.left)
            right = distribute(node.right)

            self.summ += abs(left) + abs(right)

            if left + right + node.val == 1:
                return 0
            else:
                return left + right + node.val - 1

        distribute(root)

        return self.summ