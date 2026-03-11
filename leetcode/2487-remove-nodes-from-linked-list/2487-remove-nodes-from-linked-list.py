# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
        stack.reverse()

        head = ListNode(stack.pop())
        curr = head
        while stack:
            node = ListNode(stack.pop())
            curr.next = node
            curr = curr.next

        return head