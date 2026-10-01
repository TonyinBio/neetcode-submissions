# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head or not head.next or not head.next.next: return False
        fast = slow.next.next
        while slow != fast:
            if not slow.next or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True