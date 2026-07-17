# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        total_sum = 0
        curr = head
        while curr:
            total_sum = (total_sum << 1) | curr.val
            curr = curr.next
        return total_sum