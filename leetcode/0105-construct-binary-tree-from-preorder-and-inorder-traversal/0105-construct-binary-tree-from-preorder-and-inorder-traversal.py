# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp = {num: i for i, num in enumerate(inorder)}

        self.index = 0
        def build(left, right):
            if left > right:
                return None

            node = TreeNode(preorder[self.index])
            self.index += 1

            node.left = build(left, mapp[node.val] - 1)
            node.right = build(mapp[node.val] + 1, right)

            return node

        return build(0, len(preorder) - 1)