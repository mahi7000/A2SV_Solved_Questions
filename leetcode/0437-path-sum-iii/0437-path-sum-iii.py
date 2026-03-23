# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def path(root, targetSum, summ):
            if not root:
                return 0

            count = 0
            summ += root.val
            if summ == targetSum:
                count += 1

            return count + path(root.left, targetSum, summ) + path(root.right, targetSum, summ)

        

        return path(root, targetSum, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)