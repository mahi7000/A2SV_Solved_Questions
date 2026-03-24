# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)

        left, right = 0, len(arr) - 1
        while left < right:
            summ = arr[left] + arr[right]
            if summ == k:
                return True
            if summ > k:
                right -= 1
            else:
                left += 1

        return False