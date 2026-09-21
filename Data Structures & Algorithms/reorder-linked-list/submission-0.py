# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head

        def helper(right):
            nonlocal left

            if right is None:
                return

            helper(right.next)

            if left is None:
                return

            # Odd length: left and right meet
            if left is right:
                left.next = None
                left = None
                return

            # Even length: left and right are adjacent
            if left.next is right:
                right.next = None
                left = None
                return

            next_left = left.next
            left.next = right
            right.next = next_left
            left = next_left

        helper(head)