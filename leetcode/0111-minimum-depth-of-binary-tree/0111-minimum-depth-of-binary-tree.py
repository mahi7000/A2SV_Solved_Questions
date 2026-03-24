# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, par):
            if not node:
                return 0 if not (par.right or par.left) else inf

            return min(dfs(node.left, node), dfs(node.right, node)) + 1
        

        return dfs(root, None)